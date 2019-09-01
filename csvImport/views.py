from django.shortcuts import render
from django.contrib import messages
import csv, io
from csvImport.models import Product

from django.http import HttpResponse

def index(request):
    #return HttpResponse('Hello, world!')
    template = 'product_upload.html'
    prompt={}

    if request.method == "GET":
        return render(request, template,prompt)

    csvFile = request.FILES['file']

    if not csvFile.name.endswith('.csv'):
        messages.error(request, 'Это не csv файл.')

    data = csvFile.read().decode('UTF-8')
    io_string = io.StringIO(data)
    next(io_string)
    for row in csv.reader(io_string, delimiter=';'):
        # row=rows[0].split(';')
        if row[0] != 'Код':
            product = Product()
            product.id = row[0]
            product.title = row[1]
            product.level1 = row[2]
            product.level2 = row[3]
            product.level3 = row[4]
            product.price = 0.0
            product.priceSP = 0.0
            product.quantity = 0.0
            row[5] = row[5].replace(',', '.')
            if row[5] != '':
                product.price = float(row[5])
            if row[6] != '':
                row[6] = row[6].replace(',', '.')
                product.priceSP = float(row[6])
            if row[7] != '':
                row[7] = row[7].replace(',', '.')
                product.quantity = float(row[7].replace(',', '.'))
            product.property = row[8]
            product.joint = row[9]
            product.units = row[10]
            product.pic = row[11]
            product.show = row[12]
            product.description = row[13]

            product.save()
    context = {}
    return render(request, template, context)
# Create your views here.
def results(request):

    products=Product.objects.all()
    context={'products':products}
    template='product.html'
    return render(request,template,context)


