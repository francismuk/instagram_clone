from django.db import models
from django.contrib.auth.models import User

import datetime as dt
# Create your models here.

class Profile(models.Model):
    bio = models.TextField(max_length=200, null=True, blank=True, default="bio")
    profilepic = models.ImageField(upload_to='image/', null=True, blank=True)
    user = models.OneToOneField(User, blank=True, related_name="profile")
    followers = models.ManyToManyField(User, related_name="followers", blank=True)
    following = models.ManyToManyField(User, related_name="following", blank=True)
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
        
    def is_following(self, checkuser):
        return checkuser in self.following.all()

    def followers_number(self):
        if self.followers.count():
            return self.followers.count()
        else:
            return 0

    def following_number(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0

class Category(models.Model):
    photo_category = models.CharField(max_length=50)
    
    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()
    
    def update_category(self):
        self.update_category()
        
    @classmethod
    def get_category_id(cls, id):
        category = Category.objects.get(pk = id)
        return category

    def __str__(self):
        return self.photo_category
    

    
class Location(models.Model):
    image_location = models.CharField(max_length=50)
    
    @classmethod
    def get_all_locations(cls):
        all_locations = Location.objects.all()
        return all_locations
    
    def __str__(self):
        return self.image_location

from tinymce.models import HTMLField
class Image(models.Model):
    image = models.ImageField(upload_to = 'image/',)
    name = models.CharField(max_length=60)
    post = HTMLField()
    poster = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, related_name="images")
    location = models.ForeignKey(Location, blank=True)
    category = models.ForeignKey(Category,blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
        
    def update_image(self):
        self.update_image()
        
    @classmethod
    def get_all_images(cls):
        all_images = Image.objects.all()
        return all_images
        
    @classmethod
    def get_image_by_id(cls,id):
        my_image = Image.objects.get(id=id)
        return my_image
    
    @classmethod
    def search_image(cls,search_category):
        images_category = Image.objects.filter(search_category=search_category)
        return images_category

    @classmethod
    def filter_by_category(cls, filter_category):
        images_category = Image.objects.filter(category__id=filter_category)
        return images_category   
        
    def __str__(self):
        return self.name
    
class Subscriber(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    