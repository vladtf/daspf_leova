from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, null=False)
    body = models.TextField(null=True, default='Postare fără conținut')
    created_at = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True, default='placeholder.jpg')

    def __str__(self):
        return self.title

    @property
    def get_date(self):
        time = datetime.now()
        if self.created_at.day == time.day:
            return str(time.hour - self.created_at.hour) + " ore"
        else:
            if self.created_at.month == time.month:
                return str(time.day - self.created_at.day) + " zile"
            else:
                if self.created_at.year == time.year:
                    return str(time.month - self.created_at.month) + " luni"
        return self.created_at

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = '/images/placeholder.png'
        return url


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, default='placeholder.jpg')