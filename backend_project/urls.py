
from django.contrib import admin
from django.urls import path,include


from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  
    path('',include('Data_app.urls')),
    path('admin/', admin.site.urls),
    path('ping-me/',include(('django_ping_me.urls','ping_me')))

]
