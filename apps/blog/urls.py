from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.blog.views import (
    BlogCreateView,
    BlogItemView,
    BlogListView,
    CategoryViewSet,
    CommentsCreateView,
    CommentsItemView,
    CommentsListView,
)

router = DefaultRouter(trailing_slash=False)
router.register(
    r"blog/categories",
    CategoryViewSet,
    basename="category",
)

urlpatterns = [
    path("blog", BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>", BlogItemView.as_view(), name="blog_item"),
    # Milestone 1, task 3
    path("blog/create", BlogCreateView.as_view(), name="blog_create"),
    # Milestone 1, task 6
    path("comments", CommentsListView.as_view(), name="comments_list"),
    path("comments/<int:pk>", CommentsItemView.as_view(), name="comments_item"),
    path("comments/create", CommentsCreateView.as_view(), name="comments_create"),
    *router.urls,
]
