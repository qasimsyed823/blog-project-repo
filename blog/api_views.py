# blog/api_views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .models import Post
from .serializer import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]  # token auth
    permission_classes = [IsAuthenticatedOrReadOnly]  # only authenticated can write

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # automatically assign author


#token Key=5e241e5cb9abea4f108e99f030064fb74c9fae4e
