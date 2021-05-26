from django.contrib import admin

# Register your models here.
from .models import catgory_list,post_models,coverimgapi
admin.site.register(catgory_list)
admin.site.register(post_models)
admin.site.register(coverimgapi)







