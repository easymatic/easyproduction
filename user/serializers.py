from user.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['first_name', 'last_name', 'email', 'date_joined']
        model = User
