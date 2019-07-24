from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .email import send_welcome_email
from .forms import SubscribeForm, NewPostForm, CommentForm
from django.contrib.auth.models import User
from .models import Subscriber, Image, Location, Category, Comments
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    title = 'Home'
    current_user = request.user
    comments = Comments.get_comment(Comments, id)
    if request.method == 'POST':
        formc = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']

            comment = Comment()
            comment.image = image
            comment.user = current_user
            comment.comment = comment
            comment.save()

    else:
        formc = CommentForm()

    
    
    if request.GET.get('location'):
        images = Image.filter_by_location(request.GET.get('location'))

    
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

    return render(request,'index.html', {'title':title, 'images':images, 'letterForm':form, 'commentForm':formc, 'comments':comments })


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