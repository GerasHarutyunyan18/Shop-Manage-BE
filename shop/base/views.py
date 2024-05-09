from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .utils.errors import MethodNotAllowed, UserExist, UserNotExist, InvalidLoginCreds, AccessDenied
from .utils.constants import SECRET_KEY
from django.core.mail import send_mail
from .utils.helpers import generateUserPassword
from .serializers.user import userSerializer
import datetime
import jwt
from .utils.validators import signUpValidation, marketCreationValidation, userCreationValidation
from .models import User, Market
from django.contrib.auth.hashers import make_password, check_password
import json

# Auth service class
class AuthView:
    @csrf_exempt
    def signUp(request):
        if request.method != "POST":
            return JsonResponse(MethodNotAllowed)

        data = json.loads(request.body)
        res = signUpValidation(data)
        
        if res['errors']:
            del res['result']
            return JsonResponse(res)

        result = res['result']

        result['password'] = make_password(result['password'])

        user = None
        try:
            user = User.objects.get(email=result['email'])
        except User.DoesNotExist:
            pass

        if user:
            return JsonResponse(UserExist)

        token_payload = {
            'user_id': "this is just for authenticating user in my system",
            'exp': datetime.datetime.now() + datetime.timedelta(days=5) 
        }

        token = jwt.encode(
            token_payload,
            SECRET_KEY,
            algorithm='HS256'
        )
        result['token'] = token
        
        user = User.objects.create(**result)

        return JsonResponse({"success": True})

    @csrf_exempt
    def signIn(request):
        if request.method != "POST":
            return JsonResponse(MethodNotAllowed)

        data = json.loads(request.body)

        email = data.get('email')
        password = data.get('password')

        user = None
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse(UserNotExist)

        if check_password(password=password, encoded=user.password):
            token_payload = {
            'user_id': user.pk,
            'exp': datetime.datetime.now() + datetime.timedelta(days=5) 
            }

            token = jwt.encode(
                token_payload,
                SECRET_KEY,
                algorithm='HS256'
            )
            
            user = userSerializer(user)
            return JsonResponse({"success": True, "token": token, "user": user})
        return JsonResponse(InvalidLoginCreds)


    @csrf_exempt
    def decodeUserAuthToken(request, token):
        if request.method != 'GET':
            return JsonResponse(MethodNotAllowed)

        token_data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_id = token_data.get('user_id', None)

        if user_id is None:
            return JsonResponse(UserNotExist)

        user = None
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return JsonResponse(UserNotExist)

        user = userSerializer(user)

        return JsonResponse({"success": True, "user": user})
# Auth service end

# User service class
class UserView:
    @csrf_exempt
    def createUser(request):
        if request.method != 'POST':
            return JsonResponse(MethodNotAllowed)

        data = json.loads(request.body)
        result = userCreationValidation(data)

        if result['errors']:
            del result['result']
            return JsonResponse(result)

        result = result['result']

        creator = None
        try:
            creator = User.objects.get(token=result['creatorToken'])
            # if not creator.role or creator.role.name != 'owner':
            #     return JsonResponse(AccessDenied)
        except User.DoesNotExist:
            return JsonResponse(UserNotExist)

        del result['creatorToken']
        password = generateUserPassword(6)
        result['password'] = make_password(generateUserPassword(6))

        token_payload = {
            'user_id': "this is just for authenticating user in my system",
            'exp': datetime.datetime.now() + datetime.timedelta(days=5) 
        }

        token = jwt.encode(
            token_payload,
            SECRET_KEY,
            algorithm='HS256'
        )
        subject = 'Neighbors- signup verifaction'
        message = f'Your password is - {password}'
        sender = 'neighborseandg@gmail.com'
        recipient = result['email']
        
        send_mail(subject, message, sender, [recipient])

        result['token'] = token
        user = User.objects.create(**result)
        
        return JsonResponse({'success': True, "id": user.pk})

    @csrf_exempt
    def getMe(request, token):
        if request.method != 'GET':
            return JsonResponse(MethodNotAllowed)

        user = None
        try:
            user = User.objects.get(token=token)
        except User.DoesNotExist:
            return JsonResponse(UserNotExist)

        result = userSerializer(user)
        return JsonResponse({"success": True, "user": result})
# User service end

# Market service class 
class MarketView:
    @csrf_exempt
    def createMarket(request):
        if request.method != "POST":
            return JsonResponse(MethodNotAllowed)

        data = json.loads(request.body)
        res = marketCreationValidation(data)
        
        if res['errors']:
            del res['result']
            return JsonResponse(res)

        result = res['result']

        user = None
        try:
            user = User.objects.get(token=result['ownerToken'])
            if not user.role or user.role.name != 'owner':
                return JsonResponse(AccessDenied)
        except User.DoesNotExist:
            return JsonResponse(AccessDenied)
            
        result['owner'] = user
        del result['ownerToken']
        market = Market.objects.create(**result)

        return JsonResponse({'success': True, "id": market.pk})
# Market service end 
