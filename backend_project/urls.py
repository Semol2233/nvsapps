
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
  
    path('',include('Data_app.urls')),
    path('admin/', admin.site.urls),

]
