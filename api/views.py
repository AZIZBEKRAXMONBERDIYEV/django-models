from django.http import JsonResponse, HttpRequest

from .models import Product
# from django.forms.models import model_to_dict

def model_to_dict(instance: Product) -> dict:
    return {
        'id': instance.id,
        'name': instance.name,
        'description': instance.description,
    }


def products(request: HttpRequest) -> JsonResponse:
    products = Product.objects.all()

    data = {'products': [model_to_dict(product) for product in products]}

    return JsonResponse(data)