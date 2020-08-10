from django.contrib import admin

# Register your models here.
from .models import profile
from .models import post , comment


admin.site.register(profile)
admin.site.register(post)
admin.site.register(comment)