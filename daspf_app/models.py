from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200, null=False)
    category = models.CharField(max_length=200, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
