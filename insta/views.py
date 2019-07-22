from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404
import datetime as dt

# Create your views here.
def index(request):
    title = 'Home'

    return render(request,'index.html', {'title':title})