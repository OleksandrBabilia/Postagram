from rest_framework import serializers

from .models import User
from core.abstract.serializers import AbstractSerializer

class UserSerializer(AbstractSerializer):
    class Meta:
        model = User
        fields =['id', 'username', 'first_name',
            'last_name', 'bio', 'avatar', 'email',
            'is_active', 'created', 'updated']
        read_only_field = ['is_active']