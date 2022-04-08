from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'users'
        
class Publisher(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'publishers'
