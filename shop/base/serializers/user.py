from ..models import User

def userSerializer(data: User):
    result = {}
    result['id'] = data.pk
    result['name'] = data.name
    result['surname'] = data.surname
    result['email'] = data.email
    result['image'] = data.image
    result['token'] = data.token

    return result