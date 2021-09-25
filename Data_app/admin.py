from django.contrib import admin
admin.site.site_header = "NBOX"
# Register your models here.
from .models import catgory_list,post_models,coverimgapi,msgview,nbox_ad,appsupdate,feturedchannel
admin.site.register(catgory_list)
admin.site.register(post_models)
admin.site.register(coverimgapi)
admin.site.register(nbox_ad)
admin.site.register(msgview)
admin.site.register(appsupdate)
admin.site.register(feturedchannel)













