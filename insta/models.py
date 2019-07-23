from django.db import models
from django.contrib.auth.models import User


# Create your models here.
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
    
class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    
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
    image = models.ImageField(upload_to = 'image/')
    name = models.CharField(max_length=60)
    post = HTMLField()
    caption = models.TextField()
    tags = models.ManyToManyField(tags)
    poster = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, related_name="images")
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
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
    