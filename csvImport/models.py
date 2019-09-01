from django.db import models

# Create your models here.
class Product(models.Model):
    id=models.CharField(max_length=10,primary_key=True)
    title=models.CharField(max_length=256)
    level1=models.CharField(max_length=256)
    level2=models.CharField(max_length=256)
    level3 = models.CharField(max_length=256,default='нет')
    price=models.DecimalField(max_digits=6,decimal_places=2)
    priceSP=models.DecimalField(max_digits=6,decimal_places=2)
    quantity=models.DecimalField(max_digits=10,decimal_places=2)
    property=models.CharField(max_length=256,default='нет')
    joint=models.CharField(max_length=256,default='нет')
    UNITS_CHOICES=(("шт","штука"),("упак","упаковка"),("рул","рулон"),("пог.м","погонный метр"),
                   ("пара","пара"),("меш","мешок"),("M2","M2"),("M3","M3"),("лист","лист"),("кг","килограмм"))
    units=models.CharField(max_length=5,choices=UNITS_CHOICES,default="шт")
    pic=models.CharField(max_length=32)
    show=models.BooleanField
    description=models.CharField(max_length=256,default='нет')

    def __str__(self):
        return self.title.encode('UTF-8')




