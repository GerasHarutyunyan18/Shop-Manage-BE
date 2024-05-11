from ..models import Product

def productSerializer(data: Product):
    result = {}
    result['id'] = data.pk
    result['name'] = data.name
    result['image'] = data.image
    result['price'] = data.price
    result['count'] = data.count
    result['currency'] = data.currency.token
    result['countMethod'] = data.countMethod.token
    
    return result