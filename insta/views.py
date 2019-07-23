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
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = Subscriber(name = name,email =email)
            recipient.save()
            HttpResponseRedirect('index')
    else:
        form = SubscribeForm()

    return render(request,'index.html', {'title':title, 'letterForm':form, })