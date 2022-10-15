from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Books(models.Model):
    title=models.CharField(max_length=150)
    author=models.CharField(max_length=150)
    options=(
        ("Fantasy","Fantasy"),
        ("Literary","Literary"),
        ("Mystery","Mystery"),
        ("Non-Fiction","Non-Fiction"),
        ("Science Fiction","Science Fiction"),
        ("Thriller","Thriller")
    )
    genre=models.CharField(max_length=150,choices=options,default="")
    favourite=models.BooleanField()
    def __str__(self):
        return self.title

class Reviews(models.Model):
    book=models.ForeignKey(Books,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    review = models.CharField(max_length=150)

