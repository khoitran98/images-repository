from django.db import models

# Create your models here.
class ImagefieldModel(models.Model): 
    title = models.CharField(max_length = 200) 
    img = models.ImageField(upload_to = "images/")

    class Meta:
        db_table = "imageupload"

class GetImage(models.Model):   
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to="media")
    class Meta:
        db_table = "gallery"