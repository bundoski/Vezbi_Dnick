from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name=models.CharField(max_length=50, null=True, blank=True)
    last_name=models.CharField(max_length=50, null=True, blank=True)
    image=models.ImageField(null=True, blank=True)
    interests=models.TextField(null=True, blank=True)
    skills=models.TextField(null=True, blank=True)
    profession=models.TextField(null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True, unique=True)

    def __str__(self):
        return self.first_name+" "+self.last_name + " (@"+self.user.username+")";

class Post(models.Model):
    title=models.CharField(max_length=50, null=True, blank=True)
    author=models.ForeignKey(Profile, on_delete=models.CASCADE)
    content=models.TextField(null=True, blank=True)
    date_created=models.DateTimeField(null=True, blank=True)
    last_modified=models.DateTimeField(null=True, blank=True)
    file=models.FileField(upload_to="files/", null=True, blank=True)

class Block(models.Model):
    blocker=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='+', null=True, blank=True)
    blocked=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='+', null=True, blank=True)

class Comment(models.Model):
    content=models.TextField()
    comment_author=models.ForeignKey(Profile,on_delete=models.CASCADE, null=True,blank=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)