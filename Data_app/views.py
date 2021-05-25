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

# DJango built in login 
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,get_user_model,login,logout
# end
from rest_framework.settings import api_settings
#social Auth 
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
# end

#user filter
from django.contrib.auth import get_user_model
User = get_user_model()
#end




#list view -> APi
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


def generate_jwt():
    encoded_jwt = jwt.encode({'key': 'custom_value'}, 'secret', algorithm='HS256').decode('utf-8')
    token = 'Bearer ' + encoded_jwt
    return token

jwt_token = generate_jwt()

    
class Tag_ddviewr(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100


class channelpost(generics.ListAPIView):
    queryset               = post_models.objects.all()
    serializer_class       = channelpost
    filter_backends        = [filters.SearchFilter]
    pagination_class       = Tag_ddviewr
    


   
class ServiceDetailAPIView(generics.RetrieveAPIView):
    queryset = post_models.objects.all()
    serializer_class = ClassItemSerializer
    lookup_field = ('channel_slug')