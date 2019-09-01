import csv
import sys
import os
from decimal import Decimal

project_dir="C:/Users/пользователь/Desktop/mysite/mysite"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE']='settings'

import django
django.setup()

from csvImport.models import Product
with open("C:/Users/пользователь/Desktop/mysite/import_0945-1.csv") as csvFile:
    data=csv.reader(csvFile,delimiter=';')
    for row in data:
    # row=rows[0].split(';')
        if row[0]!='Код':
            product=Product()
            product.id=row[0]
            product.title=row[1]
            product.level1=row[2]
            product.level2=row[3]
            product.level3=row[4]
            product.price=0.0
            product.priceSP=0.0
            product.quantity=0.0
            row[5]=row[5].replace(',','.')
            if row[5]!='':
                product.price=float(row[5])
            if row[6] != '':
                row[6]=row[6].replace(',','.')
                product.priceSP=float(row[6])
            if row[7] != '':
                row[7]=row[7].replace(',', '.')
                product.quantity=float(row[7].replace(',','.'))
            product.property=row[8]
            product.joint=row[9]
            product.units=row[10]
            product.pic=row[11]
            product.show=row[12]
            product.description=row[13]

            product.save()