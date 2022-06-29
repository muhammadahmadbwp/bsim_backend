from rest_framework import status, viewsets
from rest_framework.response import Response
from core.models import User
from core.serializers import (
    UserSerializer,
    GetUserSerializer,
    AuthUserSerializer,
    ChangePasswordSerializer,
    ChangeForgotPasswordSerializer
    )
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from django.utils import timezone
from django.template.loader import render_to_string
from utils.generate_otp import GenerateRandomNumber
from utils.send_email import SendEmail

# Create your views here.

class UserViewSet(viewsets.ViewSet):
    """Handle creating and updating user"""

    def get_queryset(self, request):
        queryset = User.objects.all()
        return queryset

    def list(self, request):
        queryset = self.get_queryset(request)
        serializer = GetUserSerializer(queryset, many=True)
        data = serializer.data
        return Response({"data":data, "success":True, "message":"data found"}, status=status.HTTP_200_OK)

    def create(self, request):
        if 'username' not in request.data:
            request.data['username'] = request.data['email']
        if request.data['role'] == 3:
            request.data['password'] = 'default_password'
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response({"data":data, "success":True, "message":"user created successfully"}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = User.objects.get(pk=pk)
        serializer = UserSerializer(instance=queryset, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response({"data":data, "success":True, "message":"user updated successfully"}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = User.objects.get(pk=pk)
        serializer = GetUserSerializer(queryset)
        data = serializer.data
        return Response({"data":data, "success":True, "message":"data found"}, status=status.HTTP_200_OK)

class AuthUserViewSet(viewsets.ModelViewSet):

    @action(methods=['POST'], permission_classes=[AllowAny, ], serializer_class=AuthUserSerializer, detail=False)
    def login(self, request):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(username=email, password=password)
        if not user:
            return Response({"data":[], "success":False, "message":"Invalid username/password. Please try again!"}, status=status.HTTP_200_OK)
        serializer = self.serializer_class(user)
        data = serializer.data
        return Response({"data":data, "success":True, "message":"user logged in successfully"}, status=status.HTTP_200_OK)

    @action(methods=['POST'], permission_classes=[IsAuthenticated, ], serializer_class=ChangePasswordSerializer, detail=False)
    def change_password(self, request):
        serializer = self.serializer_class(instance=request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response({"data": [], "success": True, "message": "user password changed successfully"}, status=status.HTTP_200_OK)

    @action(methods=['POST'], permission_classes=[AllowAny, ], detail=False)
    def send_otp_email(self, request):
        user = User.objects.get(email=request.data['email'])
        otp = GenerateRandomNumber.random_with_N_digits(4)
        # print(otp)
        user.otp = otp
        user.otp_created_at = timezone.now()
        user.save()
        email_data = dict()
        email_data['subject'] = 'reset password otp'
        email_data['message'] = render_to_string("email_templates/send_otp.html", {"otp": str(otp)})
        email_data['recipient_list'] = [user.email]
        SendEmail.send_email(email_data)
        return Response({"data": [], "success": True, "message": "otp sent successfully"}, status=status.HTTP_200_OK)

    @action(methods=['POST'], permission_classes=[AllowAny, ], serializer_class=ChangeForgotPasswordSerializer, detail=False)
    def change_forgot_password(self, request):
        queryset = User.objects.get(email=request.data['email'])
        serializer = self.serializer_class(instance=queryset, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        queryset.set_password(serializer.validated_data['new_password'])
        queryset.save()
        return Response({"data": [], "success": True, "message": "user password changed successfully"}, status=status.HTTP_200_OK)