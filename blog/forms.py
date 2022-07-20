from django import forms

from blog.models import *

class CommentForm(forms.ModelForm):
    ''' Форма комментариев '''
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']



