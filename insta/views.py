from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .email import send_welcome_email
from .forms import SubscribeForm, NewPostForm, CommentForm
from django.contrib.auth.models import User
from .models import Subscriber, Image, Location, Category, Comments, Profile
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    title = 'Home'
    current_user = request.user

    if request.GET.get('location'):
        images = Image.filter_by_location(request.GET.get('location'))

    else:
        images = Image.objects.all()

    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            recipient = Subscriber(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)
            HttpResponseRedirect('index', {"name": name})

    else:
        form = SubscribeForm()

    return render(request, 'index.html', {'title': title, 'images': images, 'letterForm': form})


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


@login_required(login_url='/accounts/login/')
def profile(request, username=None):

    if not username:
        username = request.user.username
    # images by user id
    images = Image.objects.filter(user_id=username)

    return render(request, 'profile.html', locals())


def image(request, id):

    try:
        image = Image.objects.get(pk=id)

    except DoesNotExist:
        raise Http404()

    current_user = request.user
    comments = Comments.get_comment(Comments, id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']

            commentt = Comments()
            commentt.image = image
            commentt.user = current_user
            commentt.comment = comment
            commentt.save()

    else:
        form = CommentForm()

    return render(request, 'image.html', {"image": image,'form': form,'comments': comments})


@login_required(login_url='/accounts/login/')
def profile_pages(request, username=None):
    if not username:
        username = request.user.username
    images = Image.objects.filter(poster_id=username)

    return render (request, 'users.html', {'images':images, 'username': username})

@login_required(login_url='/accounts/login/')
def edit_user(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdatebioForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('homePage')

    else:
        form = UpdatebioForm()
    return render(request, 'registration/edit_profile.html', {"form": form})