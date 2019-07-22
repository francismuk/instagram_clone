from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to = 'image/')
    name = models.CharField(max_length=60)
    caption = models.TextField()
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