from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # variables are used to create routes for directing the web page to detail of specific posts.
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/update/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about')
]

# <app>/<model>_<viewtype>.html
# int:pk is used to grab the object ID of post from URL to display the DetailView of that post object iD.
