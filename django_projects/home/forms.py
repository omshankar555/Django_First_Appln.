from django import forms
from home.models import Post

class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a comment...'
        }
    ))

    class Meta:
        model = Post
        fields = ('post',)

"""
class ReplyForm(forms.ModelForm):
    reply = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a comment...'
        }
    ))

    class Meta:
        model = Post
        fields = ('reply',)

"""