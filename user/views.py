from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from user.models import User
from user.serializers import UserSerializer

from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
        serializer_class = UserSerializer
        queryset = User.objects.order_by('-date_joined')


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def current_user(request, format=None):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
