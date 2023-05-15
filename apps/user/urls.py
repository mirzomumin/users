from django.urls import path, include
from rest_framework import routers

from apps.user.views.user import UserViewSet

app_name = 'user'

router = routers.DefaultRouter()
router.register('', UserViewSet, basename='user')

urlpatterns = [
    path('users/', include(router.urls)),
]
