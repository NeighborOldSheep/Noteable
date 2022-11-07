from django.db import models

# Create your models here.
class Psychology(models.Model):
    title = models.CharField(max_length = 50) #chapter title
    notes = models.TextField(default = "") #notes
    intro = models.CharField(max_length = 288,default = "") # breif intorduce of chapter
    """ notes = models.TextField(default="") #notes """


    #to show the title name in the backend
    def __str__(self):
        return self.title[:50]

class Economics(models.Model):
    title = models.CharField(max_length = 50) #chapter title
    notes = models.TextField(default = "")  #notes
    intro = models.CharField(max_length = 288,default = "") # breif intorduce of chapter
    """ notes = models.TextField(default="") #notes """

    #to show the title name in the backend
    def __str__(self):
        return self.title[:50]

class Human_Geography(models.Model):
    title = models.CharField(max_length = 50) #chapter title
    notes = models.TextField(default = "") #notes
    intro = models.CharField(max_length = 288,default = "") # breif intorduce of chapter
    """ notes = models.TextField(default="") #notes """

    #to show the title name in the backend
    def __str__(self):
        return self.title[:50]

class Seminar(models.Model):
    title = models.CharField(max_length = 50) #chapter title
    notes = models.TextField(default = "") #notes
    intro = models.CharField(max_length = 288,default = "") # breif intorduce of chapter
    """ notes = models.TextField(default="") #notes """

    #to show the title name in the backend
    def __str__(self):
        return self.title[:50]

class Env_science(models.Model):
    title = models.CharField(max_length = 50) #chapter title
    notes = models.TextField(default = "") #notes
    intro = models.CharField(max_length = 288,default = "") # breif intorduce of chapter
    """ notes = models.TextField(default="") #notes """

    #to show the title name in the backend
    def __str__(self):
        return self.title[:50]

class World_history(models.Model):
    title = models.CharField(max_length = 50) #chapter title
    notes = models.TextField(default = "") #notes
    intro = models.CharField(max_length = 288,default = "") # breif intorduce of chapter
    """ notes = models.TextField(default="") #notes """

    #to show the title name in the backend
    def __str__(self):
        return self.title[:50]

