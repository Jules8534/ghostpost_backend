from django import forms
from .models import Post

class Post_form(forms.Form):
    post_type = forms.ChoiceField(label='Boast or Roast?', choices=[('Boast', 'Boast'), ('Roast', 'Roast')], required=True)
    text = forms.CharField(label='Post', max_length=280, required=True, widget=forms.Textarea)