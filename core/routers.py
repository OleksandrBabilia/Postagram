from rest_framework import routers

from .user.viewsets import UserViewSet


router = routers.SimpleRouter()

router.register(r'users', UserViewSet, basename='user')

urlpattern = [
    *router.urls,
]