import json
from datetime import datetime

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from members.models      import Publisher
from products.models     import Detail, Funding, Product
from products.validators import validate_publisher

class ProductCreationView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            title              = data['title']
            description        = data['description']
            end_date           = data['end_date']
            target_amount      = data['target_amount']
            amount_per_session = data['amount_per_session']
            publisher_id       = data['publisher_id']
            
            publisher = Publisher.objects.get(pk=publisher_id)
            
            if (datetime.strptime(end_date, '%Y-%m-%d').date() < datetime.now().date()).days:
                return JsonResponse({'message': 'INVALID_DATE'}, status=400)
            
            product = Product.objects.create(
                title       = title,
                description = description,
                end_date    = end_date,
                publisher   = publisher
            )
            
            Detail.objects.create(
                target_amount      = target_amount,
                amount_per_session = amount_per_session,
                total_amount       = 0,
                total_quantity     = 0,
                achievement_rate   = 0,
                total_backers      = 0,
                product            = product
            )
            return JsonResponse({'message': 'SUCCESS'}, status=201)
            
        except ValueError:
            return JsonResponse({'message': 'VALUE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Publisher.DoesNotExist:
            return JsonResponse({'message': 'NO_PUBLISHER_FOUND'}, status=404)

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product = Product.objects.select_related('detail', 'publisher').get(pk=product_id)

            data = {
                'product_id'      : product.id,
                'product_title'   : product.title,
                'description'     : product.description,
                'publisher_id'    : product.publisher.id,
                'publisher_name'  : product.publisher.name,
                'target_amount'   : format(product.detail.target_amount, ',') + '???',
                'total_amount'    : format(product.detail.total_amount, ',') + '???',
                'achievement_rate': str(product.detail.achievement_rate) + '%',
                'd-day'           : str((product.end_date - datetime.now().date()).days) + '???',
                'total_backers'   : str(product.detail.total_backers) + '???'
            }
            return JsonResponse({'message': 'SUCCESS', 'data': data}, status=200)
        
        except Product.DoesNotExist:
            return JsonResponse({'message': 'NO_PRODUCT_FOUND'}, status=404)

class ProductListView(View):
    def get(self, request):
        try:
            sort   = request.GET.get('order_by', 'id')
            search = request.GET.get('search', None)

            q = Q()
            if search:
                q = Q(title__icontains=search)

            sort_set = {
                'id'                     : 'id',
                'created_ascending'      : 'created_datetime',
                'created_descending'     : '-created_datetime',
                'total_amount_ascending' : 'detail__total_amount',
                'total_amount_descending': '-detail__total_amount'
            }

            products = Product.objects.select_related('detail', 'publisher').filter(q).order_by(sort_set[sort])

            data = [{
                'product_id'      : product.id,
                'product_title'   : product.title,
                'publisher_id'    : product.publisher.id,
                'publisher_name'  : product.publisher.name,
                'total_amount'    : format(product.detail.total_amount, ',') + '???',
                'achievement_rate': str(product.detail.achievement_rate) + '%',
                'd-day'           : str((product.end_date - datetime.now().date()).days) + '???',
            } for product in products]
            return JsonResponse({'message': 'SUCCESS', 'data': data}, status=200)
        
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

class ProductManageView(View):
    def patch(self, request, product_id):
        data = json.loads(request.body)
        
        publisher_id = data['publisher_id']
        product      = Product.objects.select_related('detail').get(pk=product_id)
        
        if not validate_publisher(product_id, publisher_id):
            return JsonResponse({'message': 'FORBIDDEN'}, status=403)
        
        title              = data.get('title', product.title)
        description        = data.get('description', product.description)
        end_date           = data.get('end_date', product.end_date)
        amount_per_session = data.get('amount_per_session', product.detail.amount_per_session)
        
        if type(end_date) == str:
            if datetime.strptime(end_date, '%Y-%m-%d').date() < datetime.now().date():
                return JsonResponse({'message': 'INVALID_DATE'}, status=400)
        
        Product.objects.filter(pk=product_id).update(
            title       = title,
            description = description,
            end_date    = end_date
        )
        
        Detail.objects.filter(product_id=product.id).update(
            amount_per_session = amount_per_session
        )
        return JsonResponse({'message': 'UPDATED'}, status=200)

    def delete(self, request, product_id):
        publisher_id = json.loads(request.body).get('publisher_id')
        product      = Product.objects.get(pk=product_id)
        
        if not validate_publisher(product_id, publisher_id):
            return JsonResponse({'message': 'FORBIDDEN'}, status=403)
            
        product.delete()
        return JsonResponse({'message': 'NO_CONTENT'}, status=204)

class FundingView(View):
    def post(self, request, product_id):
        data = json.loads(request.body)

        backer_id = data['backer_id']
        quantity  = data['quantity']
        
        product = Product.objects.select_related('detail').get(pk=product_id)
        
        if product.end_date < datetime.now().date():
            return JsonResponse({'message': 'FUNDING_HAS_BEEN_CLOSED'}, status=403)
        
        if quantity <= 0:
            return JsonResponse({'message': 'INVALID_QUANTITY'}, status=400)
        
        funding, created = Funding.objects.get_or_create(
            product   = product,
            backer_id = backer_id,
            defaults  ={
                'quantity': quantity
            }
        )
        
        def detail_update():
            product.detail.total_quantity += quantity
            product.detail.total_amount += product.detail.amount_per_session * quantity
            product.detail.achievement_rate = product.detail.total_amount / product.detail.target_amount * 100
            product.detail.save()
        
        if created:
            product.detail.total_backers += 1
            detail_update()

        else:
            funding.quantity += quantity
            funding.save()
            detail_update()
        return JsonResponse({'message': 'UPDATED'}, status=200)
