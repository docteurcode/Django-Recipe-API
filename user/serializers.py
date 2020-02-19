from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'password',
                  'first_name', 'is_active',
                  'is_staff', 'last_login', 'date_joined']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(
        style={'input_type': "password"},
        trim_whitespace=False
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(request=self.context.get(
            'request'), username=username, password=password)
        if not user:
            msg = _('Please check your username and password')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs
