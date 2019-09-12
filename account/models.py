from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    pic = models.ImageField(upload_to='pics', blank=True)

    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
