from django.db import models

class Backer(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'backers'
        
class Publisher(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'publishers'
