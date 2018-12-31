from django.contrib import admin
from .models import *
# Register your models here.
from .forms import *


#class PostAdmin(admin.ModelAdmin):
#	prepopulated_fields = {'slug':('date',)}

#admin.site.register(Lesson, PostAdmin)
admin.site.register(Lesson)