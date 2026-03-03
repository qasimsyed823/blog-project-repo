from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'published', 'author', 'created_at']
    
    def update(self, instance, validated_data):
        # Make sure author does not get changed
        validated_data.pop('author', None)
        return super().update(instance, validated_data)
    