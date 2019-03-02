"""easyproduction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.authtoken import views

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from user.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

#  urlpatterns = [
    #  path('admin/', admin.site.urls),
    #  url(r'^api-auth/', include('rest_framework.urls'))
#  ]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/(?P<version>(v1))/', include(router.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token)

]
