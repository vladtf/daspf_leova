from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from daspf_app.enums import MessageStatus


class Page(models.Model):
    name = models.CharField(max_length=200, null=False)
    body = models.TextField(null=True, default='Pagină fără conținut')

    def __str__(self):
        return self.name


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
    def get_short_date(self):
        return short_date(self.created_at)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = '/images/placeholder.png'
        return url

    @property
    def get_post_images(self):
        images = PostImage.objects.filter(post=self)
        return images


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, default='placeholder.jpg')


class Message(models.Model):
    email = models.EmailField(null=False, max_length=50)
    phone = PhoneNumberField(null=True)
    name = models.CharField(null=False, max_length=50)
    text = models.CharField(null=False, max_length=500)
    response = models.CharField(null=True, max_length=500)

    status = models.CharField(max_length=1, choices=MessageStatus.choices, default=MessageStatus.NEW)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email + ' - ' + str(self.created_at)

    # def save(self, *args, **kwargs):
    #     self.updated_at = datetime.now(timezone.utc)
    #     return super(Message, self).save(*args, **kwargs)

    @property
    def get_status(self):
        return MessageStatus(self.status).label

    @property
    def get_short_date(self):
        return short_date(self.created_at)

    @property
    def get_update_date(self):
        return self.updated_at.astimezone(tz=None).strftime("%d.%m.%Y %H:%M")

    def default_response(self):
        response = 'Bună ' + self.name + '!\n\n' \
                                         'Vă mulțumim că ne-ați contactat.\n\n' \
                                         'Acesta este un mesaj automat, veți fi contactat în cel mai apropiat timp.\n\n' \
                                         'Cu respect,\n' \
                                         'Direcția Asistență Socială și Protecția Familiei, Leova'
        return response


def short_date(date):
    time_delta = timezone.now() - date

    if time_delta.total_seconds() < 3600:
        return str(time_delta.seconds // 60) + " minute"

    if time_delta.days < 1:
        return str(time_delta.seconds // 3600) + " ore"

    if time_delta.days < 30:
        return str(time_delta.days) + " zile"

    return date.strftime("%d.%m.%Y %H:%M")
