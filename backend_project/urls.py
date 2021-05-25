
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  
    path('',include('Data_app.urls')),
    path('admin/', admin.site.urls),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
