from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from Data_app import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)


urlpatterns = [
    path('homepage/<category>', channelpost.as_view()),
    path('plyerpage/<category>', playerpagecatgory.as_view()),

    path('d/<channel_slug>', ServiceDetailAPIView.as_view()),
    path('mix', mixchannel.as_view())



    
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




#mix url - its player niche prthom akta mix channel hbe 
#d/ player page dtls pagfe
#cat catagory ghulo get kora

