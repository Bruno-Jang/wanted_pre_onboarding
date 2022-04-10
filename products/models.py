from django.db import models

from utils.time_stamp import TimeStampModel
from members.models   import Backer, Publisher

class Product(TimeStampModel):
    title       = models.CharField(max_length=50)
    description = models.TextField()
    end_date    = models.CharField(max_length=20)
    publisher   = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    backer      = models.ManyToManyField(Backer, through='Funding')
    
    class Meta:
        db_table = 'products'
        
class Detail(models.Model):
    target_amount      = models.IntegerField()
    amount_per_session = models.IntegerField()
    total_amount       = models.IntegerField()
    total_quantity     = models.IntegerField()
    achievement_rate   = models.IntegerField()
    total_backers      = models.IntegerField()
    product            = models.OneToOneField(Product, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'details'
        
class Funding(TimeStampModel):
    quantity = models.IntegerField()
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    backer   = models.ForeignKey(Backer, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table = 'fundings'
