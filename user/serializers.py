from user.models import User
from django.contrib.auth.models import Group
from rest_framework import serializers


USER_GROUP_NAME = "User"
ADMIN_GROUP_NAME = "Admin"


class RoleFieldSerializer(serializers.Serializer):
    def to_representation(self, instance):
        if Group.objects.filter(user=instance, name=ADMIN_GROUP_NAME).exists():
            return ADMIN_GROUP_NAME
        if Group.objects.filter(user=instance, name=USER_GROUP_NAME).exists():
            return USER_GROUP_NAME
        return ""

    def to_internal_value(self, data):
        if not Group.objects.filter(name=data).exists():
            raise serializers.ValidationError()
        return {'groups': Group.objects.filter(name=data)}


class UserSerializer(serializers.ModelSerializer):
    role = RoleFieldSerializer(source="*")

    def get_role(self, obj):
        if Group.objects.filter(user=obj, name=ADMIN_GROUP_NAME).exists():
            return ADMIN_GROUP_NAME
        if Group.objects.filter(user=obj, name=USER_GROUP_NAME).exists():
            return USER_GROUP_NAME
        return ""

    class Meta:
        fields = ['id', 'first_name', 'last_name',
                  'email', 'date_joined', 'role']
        model = User
