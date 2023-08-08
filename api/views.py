from django.http import JsonResponse, HttpRequest

from .models import Product
from django.forms.models import model_to_dict

import json


def product_list(request: HttpRequest) -> JsonResponse:
    if request.method == 'GET':
        products = Product.objects.all()

        data = [model_to_dict(product, fields=['id', 'name']) for product in products]

        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data_json = request.body.decode('utf-8')
        data = json.loads(data_json)

        product = Product(
            name=data['name'],
            description=data['description']
        )
        product.save()
        
        return JsonResponse(model_to_dict(product), status=201)


def product_detail(request: HttpRequest, pk: int) -> JsonResponse:
    if request.method == 'GET':
        product = Product.objects.get(id=pk)

        data = model_to_dict(product, fields=['id', 'name'])

        return JsonResponse(data)

    elif request.method == 'DELETE':
        product = Product.objects.get(id=pk)
        
        product.delete()
        
        return JsonResponse({"message": "product is deleted."}, status=205)

