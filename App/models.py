from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(blank=False, null=False, max_length=50, unique=True)
    email = models.EmailField(_('email address'), unique=True, blank=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.username)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(max_length=5)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)


class Recipe(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='user_recipe', on_delete=True)
    name = models.CharField(max_length=25, blank=False)

    def save(self, *args, **kwargs):
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.name + ":" + self.user.username


class Step(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='step_recipe', on_delete=models.CASCADE, blank=False)
    step_text = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.step_text


class Ingredient(models.Model):
    text = models.CharField(max_length=50, blank=False)
    recipe = models.ForeignKey(Recipe, related_name='ingredient_recipe', on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.text
