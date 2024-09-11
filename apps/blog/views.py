from rest_framework import generics, viewsets
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from apps.blog.models import Blog, Category, Comments
from apps.blog.serializers import BlogSerializer, CategorySerializer, CommentsSerializer
from apps.common.permissions import ReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (ReadOnly,)

    def get(self, request: Request) -> Response:
        blogs = Blog.objects.all()
        return Response(self.get_serializer(blogs, many=True).data)


class BlogItemView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (ReadOnly, IsAuthenticated)

    def get(self, request: Request, pk: int) -> Response:
        blog: Blog = get_object_or_404(Blog.objects.all(), pk=pk)
        return Response(self.get_serializer(blog).data)


# Milestone 1, task 3
class BlogCreateView(generics.CreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = (IsAuthenticated,)


# Milestone 1, task 6
class CommentsListView(GenericAPIView):
    serializer_class = CommentsSerializer
    permission_classes = (ReadOnly,)

    def get(self, request: Request) -> Response:
        comments = Comments.objects.all()
        return Response(self.get_serializer(comments, many=True).data)


class CommentsItemView(GenericAPIView):
    serializer_class = CommentsSerializer
    permission_classes = (ReadOnly, IsAuthenticated)

    def get(self, request: Request, pk: int) -> Response:
        comment: Comments = get_object_or_404(Comments.objects.all(), pk=pk)
        return Response(self.get_serializer(comment).data)


class CommentsCreateView(generics.CreateAPIView):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
    permission_classes = (IsAuthenticated,)
