from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib import auth

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from . models import Account, UserToken
from . serializers import AccountSerializer
from . authentication import *

# Create your views here.

@api_view(['POST'])
def Register(request):
    try:
        data = request.data
        passsword = data['password']
        cofirm_password = data['confirm_password']
        email = data['email']
        mobile = data['mobile']

        if passsword == cofirm_password:
            is_email_exist = Account.objects.filter(email=email).exists()
            is_mobile_exist = Account.objects.filter(mobile=mobile).exists()

            if not is_email_exist :
                if not is_mobile_exist:
                    
                    user = Account.objects.create_user(
                        first_name=data['first_name'],
                        last_name=data['last_name'],
                        email=email,
                        mobile=mobile,
                        password=make_password(passsword)
                    )
                    serializer = AccountSerializer(user, many=False)
                    response = Response()
                    response.data = {
                        'data' : serializer.data,
                        'status' : status.HTTP_200_OK
                    }
                    return response

                else:
                    response = Response()
                    response.data = {
                        'message': 'mobile alredy exist',
                        'status': status.HTTP_406_NOT_ACCEPTABLE
                    }
                    return response
            else:
                response = Response()
                response.data = {
                    'message': 'email alredy exist',
                    'status': status.HTTP_406_NOT_ACCEPTABLE
                }
                return response
        else:
            response = Response()
            response.data = {
                'message': 'password missmatch',
                'status': status.HTTP_404_NOT_FOUND
            }
            return response
        
    except:
        response = Response()
        response.data = {
            'error': 'try failed',
            'status': status.HTTP_404_NOT_FOUND
        }
        return response


@api_view(['POST'])
def login(request):
    data = request.data
    email = data['email']
    password = data['password']

    user = Account.objects.filter(email=email).first()
    print(user)

    if user is None:
        response = Response()
        response.data = {
            'message': 'invalid credentials',
            'status': status.HTTP_401_UNAUTHORIZED
        }
        return response

    if not user.check_password(password):
        response = Response()
        response.data = {
            'message': 'invalid credentials',
            'status': status.HTTP_401_UNAUTHORIZED
        }
        return response

    is_athenticated = auth.authenticate(email=email, password=password)
    print(is_athenticated)
    if is_athenticated is None:
        response = Response()
        response.data = {
            'message': 'error not authenticated'
        }
        return response
    elif is_athenticated:
        print("errree")
        access_token = create_access_token(user.id)
        refresh_token=create_refresh_token(user.id)
        print(user.id)
        UserToken.objects.create(
            user_id=user.id,
            token=refresh_token,
            expired_at=datetime.datetime.utcnow()+datetime.timedelta(days=7)
            )        
        
        response=Response()
        response.set_cookie(key='refresh_token',value=refresh_token,httponly=True)
        response.data={
            'token':access_token,
            'refresh':refresh_token,
            'id':user.id,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'email':user.email,       
            'is_admin':user.is_admin,
            'status': status.HTTP_200_OK,
        }
        # serializer=AccountSerializer(user,many=False)
        # return Response(serializer.data)
        return response
    else:
        response = Response()
        response.data = {
            'message':'user not authenticated'
        }
        return response


@api_view(['GET'])
def userlist(request):
    user = Account.objects.all()
    serializer = AccountSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['PUT', 'GET'])
@authentication_classes([JWTAuthentications])
def update_user(request, pk):
    data = request.data
    first_name = data["first_name"]
    last_name = data["last_name"]
    email = data["email"]
    mobile = data["mobile"]
    user = Account.objects.get(id=pk)
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.mobile = mobile
    user.save()
    serialiser = AccountSerializer(user, many=False)
    return Response(serialiser.data)


@api_view(['POST'])
def logout(request):
    auth.logout(request)
    response = Response()
    response.data = {
        'message': 'user logged out'
    }
    return response


@api_view(['DELETE', 'GET'])
@authentication_classes([JWTAuthentications])
def delete_user(request, pk):
    user = Account.objects.get(id=pk)
    # print(pk, user)
    # serializer = AccountSerializer(user, many=False)
    # return Response(serializer.data)
    user.delete()
    response = Response()
    response.data = {
        'message': 'account deleted'
    }
    return response