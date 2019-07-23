from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .email import send_welcome_email
from .forms import SubscribeForm, NewPostForm
from .models import Subscriber, Image, Location, Category
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    title = 'Home'
    images = Image.get_all_images()
    if request.GET.get('location'):
        images = Image.filter_by_location(request.GET.get('location'))

    elif request.GET.get('tags'):
        images = Image.filter_by_tag(request.GET.get('tags'))

    # elif request.GET.get('search_term'):
    #     images = Image.search_image(request.GET.get('search_term'))

    else:
        images = Image.objects.all()
        
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            recipient = Subscriber(name=name,email=email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('index', {"name":name})
            
    else:
        form = SubscribeForm()

    return render(request,'index.html', {'title':title, 'images':images, 'letterForm':form })


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.poster = current_user
            image.save()
        return redirect('index')

    else:
        form = NewPostForm()
    return render(request, 'registration/new_post.html', {"form": form})