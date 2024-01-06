from django.db import models

# Create your models here.
class signupmaster(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.EmailField()
    password = models.CharField(max_length=12)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    mobile = models.BigIntegerField()

class my_notes(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    my_files = models.FileField(upload_to='MyNotes')
    comments = models.TextField()

class feedback(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    sub = models.CharField(max_length=20)
    msg = models.TextField()