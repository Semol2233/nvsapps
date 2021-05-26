from django.db.models.base import Model
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
# from django.shortcuts import reverse
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.urls import reverse



class catgory_list(models.Model):
    cat_name           = models.CharField(max_length=255)
    release_date       = models.DateField(auto_now_add = True)
    cat_slug           =   models.SlugField(max_length=200)

    def __str__(self):
        return self.cat_name   


class post_models(models.Model):
    channel_name   = models.CharField(max_length=255)
    channel_slug =   models.SlugField(max_length=200)
    catgory        = models.ManyToManyField(catgory_list,blank=True)
    release_date   = models.DateField(auto_now_add = True)
    straming_url =  models.URLField(default='www.test.com')
    channel_logo   = models.FileField(upload_to="channel_logo" ,blank=True)

    def __str__(self):
        return self.channel_name    


    def get_absolute_url(self):
        return reverse('fhdf')




class coverimgapi(models.Model):
    release_date   = models.DateField(auto_now_add = True)
    channel_logo   = models.FileField(upload_to="coverimg" ,blank=True)