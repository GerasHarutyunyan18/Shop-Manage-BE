from ..models import Market

def marketSerializer(data: Market):
    result = {}
    result['id'] = data.pk
    result['name'] = data.name
    result['image'] = data.image
    result['createdAt'] = data.createdAt.strftime('%Y-%m-%d')
    result['workingTimeStart'] = data.workingTimeStart.strftime('%H:%M')
    result['workingTimeEnd'] = data.workingTimeEnd.strftime('%H:%M')
    result['workersCount'] = data.getWorkersCount()
    result['totalBalance'] = data.getTotalBalance()
    
    return result