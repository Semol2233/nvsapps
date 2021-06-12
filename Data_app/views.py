from django.shortcuts import render
#rest_framwork
from rest_framework import viewsets
from rest_framework import generics,permissions,mixins,filters
from rest_framework import pagination
from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser,FormParser,MultiPartParser
from django.http import HttpResponse
#end
from rest_framework.decorators import api_view
import random
import datetime
#user model
import jwt
from Data_app.models import *
#end
from datetime import datetime, timedelta
#serializer 
from Data_app.api.serializers import *
#end
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from .pagination import PaginationHandlerMixin
#setting option
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
#end
from django.contrib.auth.mixins import LoginRequiredMixin

# DJango built in login 
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,get_user_model,login,logout
# end
from rest_framework.settings import api_settings
#social Auth 

#user filter
from django.contrib.auth import get_user_model
User = get_user_model()
#end
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,DetailView,UpdateView


from django import forms
#list view -> APi
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .forms import *















def generate_jwt():
    encoded_jwt = jwt.encode({'key': 'custom_value'}, 'secret', algorithm='HS256').decode('utf-8')
    token = 'Bearer ' + encoded_jwt
    return token

jwt_token = generate_jwt()

    
class Tag_ddviewr(pagination.PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 100

#mixpage_cahnnel player niche
class mixchannel(generics.ListAPIView):
    queryset               = post_models.objects.all().order_by('?')[:6]
    serializer_class       = mixchannel
    


#dtls page
class ServiceDetailAPIView(generics.RetrieveAPIView):
    queryset = post_models.objects.all()
    serializer_class = ClassItemSerializer
    lookup_field = ('channel_slug')



#homepageapi
class channelpost(APIView, PaginationHandlerMixin):
    pagination_class = Tag_ddviewr

    def get(self, request, category, *args, **kwargs):
        authors = catgory_list.objects.filter(cat_slug=category).values('cat_name','cat_slug')
        if authors:
            posts = post_models.objects.filter(catgory__cat_slug=category).values('id','channel_name','channel_slug','straming_url','channel_logo','release_date').order_by('-id')

            for author in list(authors):
                response = {
                'cat_name': author['cat_name']

                }
            page = self.paginate_queryset(list(posts))
            response['List'] = page
            paginated_response = self.get_paginated_response(response)
            return JsonResponse(paginated_response.data, safe=False)
        return HttpResponse('No matching data found', status=404)



    
class Tag_dsdviewr(pagination.PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 100

#payerpage
class playerpagecatgory(APIView, PaginationHandlerMixin):
    pagination_class = Tag_dsdviewr

    def get(self, request, category, *args, **kwargs):
        authors = catgory_list.objects.filter(cat_slug=category).values('cat_name','cat_slug')
        if authors:
            posts = post_models.objects.filter(catgory__cat_slug=category).values('id','channel_name','channel_slug','straming_url','channel_logo','release_date').order_by('-id')

            for author in list(authors):
                response = {
                'cat_name': author['cat_name']

                }
            page = self.paginate_queryset(list(posts))
            response['List'] = page
            paginated_response = self.get_paginated_response(response)
            return JsonResponse(paginated_response.data, safe=False)
        return HttpResponse('No matching data found', status=404)







class postchannel(CreateView,LoginRequiredMixin):
    form_class = daildddyscosst
    model = post_models
    template_name = 'uplode_us.html'




class coverapi(generics.ListAPIView):
    queryset               = coverimgapi.objects.all()[:2]
    serializer_class       = coverapiomg
    


class nbox_adview(generics.ListAPIView):
    queryset               = nbox_ad.objects.all()[:1]
    serializer_class       = nbox_adapi
    
