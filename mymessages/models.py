from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    full_name = models.CharField(max_length=100, blank=True)  # 姓名
    birthday = models.DateField(null=True, blank=True)  # 生日
    address = models.CharField(max_length=255, blank=True)  # 地址
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)  # 個人照片

class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:50] 