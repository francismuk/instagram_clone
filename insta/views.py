from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404
import datetime as dt
from .forms import SubscribeForm

# Create your views here.
def index(request):
    title = 'Home'
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = SubscribeForm()

    return render(request,'index.html', {'title':title, 'letterForm':form, })