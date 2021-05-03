from django.db import models

# Create your models here.


class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    cnombre = models.CharField(max_length=30)
    cdireccion = models.TextField()
    itelefono = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now_add=True, null=True)
    
