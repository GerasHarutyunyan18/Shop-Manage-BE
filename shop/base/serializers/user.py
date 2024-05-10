from ..models import User

def userSerializer(data: User):
    result = {}
    result['id'] = data.pk
    result['name'] = data.name
    result['surname'] = data.surname
    result['email'] = data.email
    result['image'] = data.image
    result['token'] = data.token
    result['rate'] = data.rate
    result['birthDate'] = data.birthDate.strftime('%Y-%m-%d')
    result['role'] = data.role.name if data.role else ""

    return result