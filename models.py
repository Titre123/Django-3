from cgitb import text
from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Post"
    user = get_user_model()
    Title  = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(user, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    published_date= models.DateTimeField()