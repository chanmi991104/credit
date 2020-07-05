from django import forms
from .models import Post, Credit

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['time']

class CreditForm(forms.ModelForm):
    class Meta:
        model = Credit
        fields = ['title','credit','grade','time']