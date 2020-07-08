from django import forms

from martor.fields import MartorFormField
from blog.models import Post


class SimpleForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput())
    description = MartorFormField()


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'