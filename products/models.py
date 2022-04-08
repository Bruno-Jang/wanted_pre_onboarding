from django.db import models

from utils.time_stamp import TimeStampModel
from members.models   import Publisher, User

class Product(TimeStampModel):
    title              = models.CharField(max_length=50)
    description        = models.TextField()
    target_amount      = models.IntegerField()
    amount_per_session = models.IntegerField()
    total_amount       = models.IntegerField()
    achivement_rate    = models.IntegerField()
    end_date           = models.CharField(max_length=20)
    publisher          = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    user               = models.ManyToManyField(User, through='Funding')

    class Meta:
        db_table = 'products'
        
class Funding(TimeStampModel):
    funding_nums = models.IntegerField()
    product      = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user         = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table = 'fundings'