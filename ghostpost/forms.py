from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    BOAST_ROAST_CHOICES = [
        (True, "BOAST"),
        (False, "ROAST")
    ]
    boast = forms.ChoiceField(
        widget=forms.RadioSelect, 
        choices=BOAST_ROAST_CHOICES
    )    

    class Meta:
        model = Post
        exclude = ['up', 'down', 'score']
