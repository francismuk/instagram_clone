from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .forms import SubscribeForm

# Create your views here.
def index(request):
    title = 'Home'
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['subscriber']
            email = form.cleaned_data['email']

            recipient = SubscribeForm(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

    return render(request,'index.html', {'title':title, 'letterForm':form, })