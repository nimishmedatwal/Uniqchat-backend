from rest_framework import serializers
from .models import User
from .utils import generate_user_credentials

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uuid', 'public_key']

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uuid', 'public_key', 'password']
        read_only_fields = ['uuid', 'public_key']

    def create(self, validated_data):
        uuid, public_key, private_key = generate_user_credentials()
        user = User.objects.create_user(uuid=uuid, public_key=public_key, private_key=private_key)
        return user, private_key  # Return private key for user to store securely
