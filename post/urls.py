from django.urls import path
from post import views

'''urlpatterns = [
    path('',views.index,name='index')
]'''
from django.urls import path
from .views import (
    CreateUserView, ListUserView, RetrieveUserView, UpdateUserView, DeleteUserView,
    CreatePostView, RetrievePostView, UpdatePostView, DeletePostView,
    CreateLikeView, RetrieveLikeView, UpdateLikeView, DeleteLikeView,
    ListPostView
)

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', CreateUserView.as_view(), name='user-create'),
    path('users/<int:pk>/', RetrieveUserView.as_view(), name='user-retrieve'),
    path('users/<int:pk>/update/', UpdateUserView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', DeleteUserView.as_view(), name='user-delete'),
    path('users/list/', ListUserView.as_view(), name='user-list'),
    path('posts/', CreatePostView.as_view(), name='post-create'),
    path('posts/<int:pk>/', RetrievePostView.as_view(), name='post-retrieve'),
    path('posts/<int:pk>/update/', UpdatePostView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', DeletePostView.as_view(), name='post-delete'),
    path('likes/', CreateLikeView.as_view(), name='like-create'),
    path('likes/<int:pk>/', RetrieveLikeView.as_view(), name='like-retrieve'),
    path('likes/<int:pk>/update/', UpdateLikeView.as_view(), name='like-update'),
    path('likes/<int:pk>/delete/', DeleteLikeView.as_view(), name='like-delete'),
    path('posts/list/', ListPostView.as_view(), name='post-list'),
]

