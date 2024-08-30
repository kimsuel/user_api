from django.contrib.auth import password_validation
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.models import User, Address


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.get('password')
        try:
            if password:
                password_validation.validate_password(password)
        except Exception as e:
            raise ValidationError(e)

        instance, is_create = User.objects.get_or_create(**validated_data)

        if password:
            instance.set_password(password)
            instance.save(update_fields=['password'])

        return instance


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = ('user',)
