from django import forms
# from .models import Post


class Post_form(forms.Form):
    BOAST_ROAST_CHOICES = [
        (True, "BOAST"),
        (False, "ROAST")
    ]
    boast = forms.ChoiceField(
        widget=forms.RadioSelect, 
        choices=BOAST_ROAST_CHOICES
    )    
    
    text = forms.CharField(max_length=280)

    def __str__(self):
        return self.text
