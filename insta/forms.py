from django import forms

class SubscribeForm(forms.Form):
    subscriber = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label = 'Email')