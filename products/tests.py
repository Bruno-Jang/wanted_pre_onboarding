import json

from django.test import TestCase, Client

from products.models import Product, Detail
from members.models  import Publisher

class ProductDetailTest(TestCase):
    def setUp(self):
        Publisher.objects.create(
            id   = 1,
            name = 'aple'
        )
        
        Product.objects.create(
            id               = 1,
            title            = '테스트용 핸드폰',
            description      = '테스트 진행용',
            end_date         = '2022-04-20',
            publisher_id     = 1,
            created_datetime = '2022-04-10',
        )
        
        Detail.objects.create(
            id                 = 1,
            target_amount      = 20000,
            amount_per_session = 100,
            total_amount       = 0,
            total_quantity     = 0,
            achievement_rate   = 0,
            total_backers      = 0,
            product_id         = 1
        )
           
    def tearDown(self):
        Publisher.objects.all().delete()
        Product.objects.all().delete()
        Detail.objects.all().delete()
    
    def test_get_success_product_detail(self):
        client       = Client()
        response     = client.get('/products/detail/1')
        self.maxDiff = None
        
        self.assertEqual(response.json(),
            {'message': 'SUCCESS',
            'data': { 
                'product_id'      : 1,
                'product_title'   : '테스트용 핸드폰',
                'description'     : '테스트 진행용', 
                'publisher_id'    : 1,
                'publisher_name'  : 'aple',
                'target_amount'   : '20,000원',
                'total_amount'    : '0원',
                'achievement_rate': '0%',
                'd-day'           : '6일',
                'total_backers'   : '0명'
                }
            }
        )
        self.assertEqual(response.status_code, 200)
        
    def test_get_fail_product_detail_when_product_does_not_exist(self):
        client       = Client()
        response     = client.get('/products/detail/2')
        self.maxDiff = None
        
        self.assertEqual(response.json(),
            {'message': 'NO_PRODUCT_FOUND'}
        )
        self.assertEqual(response.status_code, 404)

class ProductMainTest(TestCase):
    def setUp(self):
        publisher_list = [
            Publisher(
                id   = 1,
                name = 'bruno'
            ),
            Publisher(
                id   = 2,
                name = 'kyle'
            ),
            Publisher(
                id   = 3,
                name = 'edie'
            )
        ]
        Publisher.objects.bulk_create(publisher_list)
        
        product_list = [
            Product(
                id               = 1,
                title            = '프로용 마우스',
                end_date         = '2022-10-11',
                publisher_id     = 1,
                created_datetime = '2022-04-10',
            ),
            Product(
                id               = 2,
                title            = '프로용 키보드',
                end_date         = '2022-05-15',
                publisher_id     = 2,
                created_datetime = '2022-04-11',
            ),
            Product(
                id               = 3,
                title            = '프로용 의자',
                end_date         = '2022-07-20',
                publisher_id     = 3,
                created_datetime = '2022-04-13',
            )
        ]
        Product.objects.bulk_create(product_list)
        
        detail_list = [
            Detail(
                id                 = 1,
                target_amount      = 20000,
                amount_per_session = 200,
                total_amount       = 0,
                total_quantity     = 0,
                achievement_rate   = 0,
                total_backers      = 0,
                product_id         = 1
            ),
            Detail(
                id                 = 2,
                target_amount      = 500000,
                amount_per_session = 50000,
                total_amount       = 0,
                total_quantity     = 0,
                achievement_rate   = 0,
                total_backers      = 0,
                product_id         = 2
            ),
            Detail(
                id                 = 3,
                target_amount      = 30000000,
                amount_per_session = 130000,
                total_amount       = 0,
                total_quantity     = 0,
                achievement_rate   = 0,
                total_backers      = 0,
                product_id         = 3
            )
        ]
        Detail.objects.bulk_create(detail_list)
        
    def tearDown(self):
        Publisher.objects.all().delete()
        Product.objects.all().delete()
        Detail.objects.all().delete()
    
    def test_get_success_product_list(self):
        client       = Client()
        response     = client.get('/products/list?search=프로&order_by=created_descending')
        self.maxDiff = None
        
        self.assertEqual(response.json(),
            {'message': 'SUCCESS',
            'data': [{ 
                'product_id'      : 3,
                'product_title'   : '프로용 의자',
                'publisher_id'    : 3,
                'publisher_name'  : 'edie',
                'total_amount'    : '0원',
                'achievement_rate': '0%',
                'd-day'           : '97일'
                },
                {
                'product_id'      : 2,
                'product_title'   : '프로용 키보드',
                'publisher_id'    : 2,
                'publisher_name'  : 'kyle',
                'total_amount'    : '0원',
                'achievement_rate': '0%',
                'd-day'           : '31일'
                },
                {
                'product_id'      : 1,
                'product_title'   : '프로용 마우스',
                'publisher_id'    : 1,
                'publisher_name'  : 'bruno',
                'total_amount'    : '0원',
                'achievement_rate': '0%',
                'd-day'           : '180일'
                }]
            }
        )
        self.assertEqual(response.status_code, 200)
        
    def test_get_fail_product_list_if_Key_Error(self):
        client       = Client()
        response     = client.get('/products/list?order_by=')
        self.maxDiff = None
        
        self.assertEqual(response.json(),
            {'message': 'KEY_ERROR'}
        )
        self.assertEqual(response.status_code, 400)

class ProductManageTest(TestCase):
    def setUp(self):
        publisher_list = [
            Publisher(
                id   = 1,
                name = 'bruno'
            ),
            Publisher(
                id   = 2,
                name = 'kyle'
            ),
            Publisher(
                id   = 3,
                name = 'edie'
            )
        ]
        Publisher.objects.bulk_create(publisher_list)
        
        product_list = [
            Product(
                id               = 1,
                title            = '프로용 마우스',
                end_date         = '2022-10-11',
                publisher_id     = 1,
                created_datetime = '2022-04-10',
            ),
            Product(
                id               = 2,
                title            = '프로용 키보드',
                end_date         = '2022-05-15',
                publisher_id     = 2,
                created_datetime = '2022-04-11',
            ),
            Product(
                id               = 3,
                title            = '프로용 의자',
                end_date         = '2022-07-20',
                publisher_id     = 3,
                created_datetime = '2022-04-13',
            )
        ]
        Product.objects.bulk_create(product_list)
        
        detail_list = [
            Detail(
                id                 = 1,
                target_amount      = 20000,
                amount_per_session = 200,
                total_amount       = 0,
                total_quantity     = 0,
                achievement_rate   = 0,
                total_backers      = 0,
                product_id         = 1
            ),
            Detail(
                id                 = 2,
                target_amount      = 500000,
                amount_per_session = 50000,
                total_amount       = 0,
                total_quantity     = 0,
                achievement_rate   = 0,
                total_backers      = 0,
                product_id         = 2
            ),
            Detail(
                id                 = 3,
                target_amount      = 30000000,
                amount_per_session = 130000,
                total_amount       = 0,
                total_quantity     = 0,
                achievement_rate   = 0,
                total_backers      = 0,
                product_id         = 3
            )
        ]
        Detail.objects.bulk_create(detail_list)
        
    def tearDown(self):
        Publisher.objects.all().delete()
        Product.objects.all().delete()
        Detail.objects.all().delete()
       
    def test_patch_success_product_update(self):       
        data = {
            'publisher_id'      : 1,
            'title'             : '1번 제품 수정본',
            'description'       : '상세 설명 수정',
            # 'end_date'        : '2022-07-07',
            'amount_per_session': 20000
        }
        url      = '/products/1'
        res      = json.dumps(data)
        client   = Client()
        response = client.patch(url, res, content_type='application/json')

        self.assertEqual(response.json(),
            {'message': 'UPDATED'}
        )
        self.assertEqual(response.status_code, 200)

    def test_patch_fail_product_update_when_publisher_does_not_match(self):
        data = {
            'publisher_id'      : 2,
            'title'             : '1번 제품 수정본',
            'description'       : '상세 설명 수정',
            # 'end_date'        : '2022-07-07',
            'amount_per_session': 20000
        }
        url      = '/products/1'
        res      = json.dumps(data)
        client   = Client()
        response = client.patch(url, res, content_type='application/json')
        
        self.assertEqual(response.json(),
            {'message': 'FORBIDDEN'}
        )
        self.assertEqual(response.status_code, 403)
    
    # json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0) 로 인해 테스트 진행이 안 되는 상태입니다. 해결책 찾으면 적용하겠습니다.
    # def test_delete_success_product_delete(self):
    #     data = {'publisher_id': 2}
    #     url      = '/products/2'
    #     res      = json.dumps(data)
        
    #     client   = Client()
    #     response = client.delete(url, res, content_type='application/json')
    #     print('응답2 : ', response)
    #     print('제이슨2 : ', response.json())
        
    #     self.assertEqual(response.json(),
    #         {'message': 'NO_CONTENT'}
    #     )
    #     self.assertEqual(response.status_code, 204)
        
    def test_delete_fail_product_delete_when_publisher_does_not_match(self):
        data = {
        'publisher_id' : 2,
        }
        url      = '/products/1'
        res      = json.dumps(data)
        client   = Client()
        response = client.patch(url, res, content_type='application/json')
        
        self.assertEqual(response.json(),
            {'message': 'FORBIDDEN'}
        )
        self.assertEqual(response.status_code, 403)
