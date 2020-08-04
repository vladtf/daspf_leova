from django import forms
from phonenumber_field.formfields import PhoneNumberField

from daspf_app.models import Post, PostImage, Message


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'category',
            'image',
        ]


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = PostImage
        fields = [
            'image'
        ]


class PostFullForm(PostForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(PostForm.Meta):
        fields = PostForm.Meta.fields + ['images']


class PageDataForm(forms.Form):
    title = forms.CharField(required=True, label='Titlu', widget=forms.TextInput(
        attrs={"class": "w-100 my-2"}
    ))
    body = forms.CharField(required=True, label='Conținut postare', widget=forms.Textarea(attrs={
        "class": "my-2 w-100",
    }))


class MessageForm(forms.ModelForm):

    name = forms.CharField(label='Nume', widget=forms.TextInput(attrs={
        "class": "w-100"
    }))

    phone = PhoneNumberField(region='MD')

    text = forms.CharField(label='Mesaj', widget=forms.Textarea(attrs={
        "class": "w-100",
    }))

    class Meta:
        model = Message
        fields = [
            'email',
            'name',
            'phone',
            'text',
        ]
