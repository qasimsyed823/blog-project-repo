from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=10000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    