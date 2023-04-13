from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status 

from core.abstract.viewsets import AbstractViewSet
from .models import Post 
from .serializers import PostSerializer


class PostViewSet(AbstractViewSet):
    http_method_names = ('post', 'get', 'put', 'delete', )
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )
    
    def get_queryset(self):
        return Post.objects.all()
    
    def get_object(self):
        obj = Post.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    