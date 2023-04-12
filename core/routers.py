from rest_framework import routers

from .user.viewsets import UserViewSet
from core.auth.viewsets import RegisterViewSet

router = routers.SimpleRouter()

router.register(r'users', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='auth-register')

urlpatterns = [
    *router.urls,
]