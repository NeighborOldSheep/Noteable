from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Psychology(models.Model):
    title = models.CharField(max_length = 50) #chapter title
    intro = models.CharField(max_length = 288,default = "") # breif intorduce of chapter
    notes = RichTextField(null=True) #notes
    
    """ notes = models.TextField(default="") #notes """


    #to show the title name in the backend
    def __str__(self):
        return self.title[:50]

class Economics(models.Model):
    title = models.CharField(max_length = 50) #chapter title
    intro = models.CharField(max_length = 288,default = "") # breif intorduce of chapter
    notes = RichTextField(null=True)  #notes
    
    """ notes = models.TextField(default="") #notes """

    #to show the title name in the backend
    def __str__(self):
        return self.title[:50]

class Human_Geography(models.Model):
    title = models.CharField(max_length = 50) #chapter title
    intro = models.CharField(max_length = 288,default = "") # breif intorduce of chapter
    notes = RichTextField(null=True) #notes
    
    """ notes = models.TextField(default="") #notes """

    #to show the title name in the backend
    def __str__(self):
        return self.title[:50]

class Seminar(models.Model):
    title = models.CharField(max_length = 50) #chapter title
    intro = models.CharField(max_length = 288,default = "") # breif intorduce of chapter
    notes = RichTextField(null=True) #notes
    
    """ notes = models.TextField(default="") #notes """

    #to show the title name in the backend
    def __str__(self):
        return self.title[:50]

class Env_science(models.Model):
    title = models.CharField(max_length = 50) #chapter title
    intro = models.CharField(max_length = 288,default = "") # breif intorduce of chapter
    notes = RichTextField(null=True) #notes
    
    """ notes = models.TextField(default="") #notes """

    #to show the title name in the backend
    def __str__(self):
        return self.title[:50]

class World_history(models.Model):
    title = models.CharField(max_length = 50) #chapter title
    intro = models.CharField(max_length = 288,default = "") # breif intorduce of chapter
    notes = RichTextField(null=True) #notes
    
    """ notes = models.TextField(default="") #notes """

    #to show the title name in the backend
    def __str__(self):
        return self.title[:50]

