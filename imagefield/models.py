from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import PositiveIntegerField

class PositiveBigIntegerField(PositiveIntegerField):
    """Represents MySQL's unsigned BIGINT data type (works with MySQL only!)"""
    empty_strings_allowed = False

    def get_internal_type(self):
        return "PositiveBigIntegerField"

    def db_type(self, connection):
        # This is how MySQL defines 64 bit unsigned integer data types
        return "bigint UNSIGNED"

class ImagesModel(models.Model): 
    title = models.CharField(max_length = 200) 
    img = models.ImageField(upload_to = "images/")
    user = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
    hash = PositiveBigIntegerField()
    class Meta:
        db_table = "images"
