from django.shortcuts import render
import requests
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Post, Like
from .serializers import UserSerializer, PostSerializer, LikeSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
#port - 7000
#canvaaccount@1009-pl1
def index(request):
    return render(request,'index.html')


from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Post, Like
from .serializers import UserSerializer, PostSerializer, LikeSerializer

#for createuser
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RetrieveUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UpdateUserView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DeleteUserView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



# add this is for handle GET req for users
class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
class CreatePostView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
from django.db.models import Prefetch
class RetrievePostView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user:
            raise PermissionDenied("You do not have permission to access this post.")
        return super().retrieve(request, *args, **kwargs)
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related(Prefetch('like_set', queryset=Like.objects.all()))
        return queryset

from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
class UpdatePostView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user:
            raise PermissionDenied("You do not have permission to update this post.")
        return super().update(request, *args, **kwargs)

class DeletePostView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user:
            raise PermissionDenied("You do not have permission to delete this post.")
        return super().destroy(request, *args, **kwargs)

class CreateLikeView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    


class RetrieveLikeView(generics.RetrieveAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related('post')
        return queryset

class UpdateLikeView(generics.UpdateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

class DeleteLikeView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

class ListPostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    
    