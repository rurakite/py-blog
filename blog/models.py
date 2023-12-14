from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='blog_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='blog_user_permissions')

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return self.username


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_time"]
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='commentary'
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ["-created_time"]
        verbose_name_plural = "Commentaries"

    def __str__(self):
        return f"{self.user.username} - {self.post.title[:20]}..."
