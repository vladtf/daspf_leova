from captcha.fields import CaptchaField
from django import forms
from phonenumber_field.formfields import PhoneNumberField

from daspf_app.models import Post, PostImage, Message, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'visible',
            'title',
            'body',
            'category',
            'image'
        ]

    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     self.fields['category'].queryset = Category.objects.filter(
    #         name__in=['Noutăți', 'Evenimente', 'Posturi vacante', 'Anunțuri'])


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
    body = forms.CharField(required=True, label='Conținut postare', widget=forms.Textarea(attrs={
        "class": "my-2 w-100",
    }))


class MessageForm(forms.ModelForm):
    name = forms.CharField(label='Nume', widget=forms.TextInput(attrs={
        "class": "w-100"
    }))

    phone = PhoneNumberField(region='MD', label='Telefon mobil', required=True)

    text = forms.CharField(label='Mesaj', max_length=500, widget=forms.Textarea(attrs={
        "class": "w-100 ",
        "style": "min-height: 220px;"
    }))

    captcha = CaptchaField()

    class Meta:
        model = Message
        fields = [
            'email',
            'name',
            'phone',
            'text',
            'captcha'
        ]


class MessageRespondForm(forms.ModelForm):
    response = forms.CharField(label='Răspuns', required=False, max_length=500, widget=forms.Textarea(attrs={
        "class": "form-control d-inline-block auto-grow",
        "style": "min-height: 220px;"
    }))

    # status = forms.ChoiceField(label='Status', widget=forms.Select(attrs={
    #     "class": "custom-select"
    # }))

    class Meta:
        model = Message
        fields = [
            'response',
            'status'
        ]
        widgets = {
            'status': forms.Select(attrs={
                "class": "custom-select"
            })
        }
