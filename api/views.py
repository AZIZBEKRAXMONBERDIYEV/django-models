from django.http import JsonResponse, HttpRequest

from .models import Product
from django.forms.models import model_to_dict

import json


def products(request: HttpRequest, pk=None) -> JsonResponse:
    if request.method == 'GET':
        if pk is None:
            products = Product.objects.all()

            data = [model_to_dict(product, fields=['id', 'name']) for product in products]

            return JsonResponse(data, safe=False)
        else:
            product = Product.objects.get(id=pk)

            data = model_to_dict(product, fields=['id', 'name'])

            return JsonResponse(data)

    elif request.method == 'POST':
        data_json = request.body.decode('utf-8')
        data = json.loads(data_json)

        product = Product(
            name=data['name'],
            description=data['description']
        )
        product.save()
        
        return JsonResponse(model_to_dict(product), status=201)