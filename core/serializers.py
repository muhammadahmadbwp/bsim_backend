from rest_framework import serializers
from core.models import User, Role
from rest_framework.authtoken.models import Token
from django.contrib.auth import password_validation


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        role = validated_data.pop('role', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        if role is not None:
            instance.role = role
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.password:
            representation.pop('password')
        return representation

class GetUserSerializer(serializers.ModelSerializer):
    # role = serializers.SerializerMethodField()
    # role = RoleSerializer(read_only=True)

    # def get_role(self, obj):
    #     queryset = Role.objects.get(id=obj.role.id)
    #     return RoleSerializer(queryset).data

    class Meta:
        model = User
        # fields = "__all__"
        exclude = ["password"]
        depth = 1


class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'auth_token', 'email', 'is_active', 'is_staff', 'is_superuser')
        read_only_fields = ('id', 'email', 'is_active', 'is_staff', 'is_superuser')

    def get_auth_token(self, obj):
        if Token.objects.filter(user=obj).exists():
            token = Token.objects.get(user=obj)
        else:
            token = Token.objects.create(user=obj)
        return token.key


class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate(self, attrs):
        # print(attrs)
        # print(self.instance)
        if not self.instance.check_password(attrs['current_password']):
            raise serializers.ValidationError('wrong password!!!')
        # password_validation.validate_password(attrs['new_password'])
        return attrs

class ChangeForgotPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)

    def validate(self, attrs):
        print(self.instance)
        if not self.instance and self.instance.otp == attrs['otp']:
            raise serializers.ValidationError('wrong otp!!!')
        return attrs