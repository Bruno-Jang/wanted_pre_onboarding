import os
import csv
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onboarding.settings')
django.setup()

from members.models  import Publisher, Backer
from products.models import Detail, Funding, Product


PUBLISHER_PATH = './csv/publisher.csv'
BACKER_PATH    = './csv/backer.csv'
PRODUCT_PATH   = './csv/product.csv'
DETAIL_PATH    = './csv/detail.csv'
FUNDING_PATH   = './csv/funding.csv'


def insert_publisher():
    with open(PUBLISHER_PATH) as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            name = row[0]
            # print(name)
            Publisher.objects.create(name = name)
    print('Publisher data was uploaded!')
    
def insert_backer():
    with open(BACKER_PATH) as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            name = row[0]
            # print(name)
            Backer.objects.create(name = name)
    print('Backer data was uploaded!')
    
def insert_product():
    with open(PRODUCT_PATH) as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            title        = row[0]
            description  = row[1]
            end_date     = row[2]
            publisher_id = row[3]
            publisher    = Publisher.objects.get(pk=publisher_id)

            Product.objects.create(
                title       = title,
                description = description,
                end_date    = end_date,
                publisher   = publisher
            )
    print('Product data was uploaded!')
    
def insert_detail():
    with open(DETAIL_PATH) as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            target_amount      = row[0]
            amount_per_session = row[1]
            total_amount       = row[2]
            total_quantity     = row[3]
            achievement_rate   = row[4]
            product_id         = row[5]
            total_backers      = row[6]
            product = Product.objects.get(pk=product_id)

            Detail.objects.create(
                target_amount      = target_amount,
                amount_per_session = amount_per_session,
                total_amount       = total_amount,
                total_quantity     = total_quantity,
                achievement_rate   = achievement_rate,
                total_backers      = total_backers,
                product            = product
            )
    print('Detail data was uploaded!')
    
def insert_funding():
    with open(FUNDING_PATH) as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            product_id = row[0]
            backer_id  = row[1]
            quantity   = row[2]

            product = Product.objects.get(pk=product_id)
            backer  = Backer.objects.get(pk=backer_id)

            Funding.objects.create(
                quantity = quantity,
                product  = product,
                backer   = backer
            )
    print('Funding data was uploaded!')


# insert_publisher()
# insert_backer()
# insert_product()
# insert_detail()
# insert_funding()
