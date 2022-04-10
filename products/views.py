import json
from MySQLdb      import IntegrityError
from django.http  import JsonResponse
from django.views import View

from members.models  import Publisher
from products.models import Detail, Product


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
            
            product = Product.objects.create(
                title       = title,
                description = description,
                end_date    = end_date,
                publisher   = publisher
            )
            # print(product)
            
            detail = Detail.objects.create(
                target_amount      = target_amount,
                amount_per_session = amount_per_session,
                total_amount       = 0,
                total_quantity     = 0,
                achievement_rate   = 0,
                total_backers      = 0,
                product            = product
            )
            # print(detail)
            return JsonResponse({'message': 'SUCCESS'}, status=201)
            
        except ValueError:
            return JsonResponse({'message': 'VALUE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except IntegrityError:
            return JsonResponse({'message': 'PRODUCT_IS_ALREADY_USED'}, status=404)
        except Publisher.DoesNotExist:
            return JsonResponse({'message': 'NO_PUBLISHER_FOUND'}, status=404)

class ProductDeletionView(View):
    def delete(self, request, product_id, publisher_id):
        try:
            product = Product.objects.get(pk=product_id)
            
            if product.publisher.id != publisher_id:
                return JsonResponse({'message': 'INVALID_PUBLISHER'}, status=404)
                
            Detail.objects.get(product=product).delete()
            product.delete()
            return JsonResponse({'message': 'NO_CONTENT'}, status=204)
        
        except Product.DoesNotExist:
            return JsonResponse({'message': 'NO_PRODUCT_FOUND'}, status=404)
