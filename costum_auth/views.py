from django.contrib.auth.models import User
# # from django.shortcuts import render
# from django.contrib.auth.password_validation import validate_password
# from django.core.exceptions import ValidationError
# from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet

from costum_auth.serializers import RegisterSerializer


class RegisterView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response({'token': str(token.key)})


class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        login = request.data.get('login')
        if not User.objects.filter(username=login).exists():
            return Response(
                f'{login} - does not exists'
            )
        user = User.objects.get(username=login)
        password = request.data.get('password')
        pass_check = user.check_password(password)
        if not pass_check:
            return Response('login or password incorrect')
        token = Token.objects.get(user=user)
        return Response({'token': str(token.key)})


# class RegisterView(APIView):
#     def post(self, request, *args, **kwargs):
#
        # login = request.data.get('login')
        # if User.objects.filter(username=login).exists():
        #     return Response(
        #         {'login': 'login already used'},
        #         status=status.HTTP_400_BAD_REQUEST
        #                     )
        # password = request.data.get('password')
        # try:
        #     validate_password(password)
        # except ValidationError as b:
        #     return Response(b)
        # user = User.objects.create(username=login)
        # user.set_password(password)
        # user.save()
        # token = Token.objects.create(user=user)
        # return Response({'token': str(token.key)})
