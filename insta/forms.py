from django import forms
from .models import Image

class SubscribeForm(forms.Form):
    name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label = 'Email')
    
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['poster', 'post_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }