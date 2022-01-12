from django.urls import path
from .views import (
    HomeView,
    ArticleDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CategoryCreateView,
    CategoryView,
    LikeView,
    CommentCreateView,
)

urlpatterns = [
    path('index',HomeView.as_view(), name="home"),
    path('article/<int:pk>',ArticleDetailView.as_view(), name="article_detail"),
    path('add_post/',PostCreateView.as_view(), name="add_post"),
    path('article/<int:pk>/add_comment/',CommentCreateView.as_view(), name="add_comment"),
    path('add_category/',CategoryCreateView.as_view(), name="add_category"),
    path('article/edit/<int:pk>',PostUpdateView.as_view(), name="update_post"),
    path('article/<int:pk>/delete',PostDeleteView.as_view(), name="delete_post"),
    path('category/<str:cats>/',CategoryView, name="category_view"),
    path('like/<int:pk>',LikeView, name="like_post")
]