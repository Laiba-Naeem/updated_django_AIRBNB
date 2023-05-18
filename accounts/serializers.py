from rest_framework import serializers
from .models import User, GoogleSignUser
# User Serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# Register Serializer


class GoogleSignSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleSignUser
        fields = '__all__'

    def create(self, validated_data):
        user = GoogleSignUser.objects.create(**validated_data)
        return user


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data['password']
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
