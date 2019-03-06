from django.conf.urls import url, include

from rest_framework import routers

from order import views


router = routers.DefaultRouter()
router.register(r'user', views.UserViewset)

urlpatterns = [
    url(r'', include(router.urls)),

]
