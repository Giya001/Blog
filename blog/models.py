from django.db import models

import account
from config.settings import AUTH_USER_MODEL


# Create your models here.
class Blog(models.Model):
    TYPES = {
        'Journal': 'Journal',
        'Life updates': 'Life updates',
        'Travel': 'Travel',
        'Personal development': 'Personal development',
        'IT': 'IT',
        'Football': 'Football',
    }
    author=models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to="blog_images", blank=True, null=True)
    style = models.CharField(max_length=50, choices=TYPES, default='Journal')
    created_at=models.DateTimeField(auto_now_add=True)
    published=models.BooleanField(default=True)


    def __str__(self):
        return self.title
