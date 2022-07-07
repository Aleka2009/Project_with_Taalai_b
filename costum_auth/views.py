from django.contrib.auth.models import User
# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token


class RegisterView(APIView):

    def post(self, request, *args, **kwargs):
        login = request.data.get('login')
        password = request.data.get('password')
        user = User.objects.create(username=login)
        user.set_password(password)
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': str(token.key)})
