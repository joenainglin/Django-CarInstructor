from django.contrib import admin
from .models import *
# Register your models here.
from .forms import *


#class PostAdmin(admin.ModelAdmin):
#	prepopulated_fields = {'slug':('date',)}

#admin.site.register(Lesson, PostAdmin)

class LeassonAdmin(admin.ModelAdmin):
	list_display = ('date','time', 'name', 'slug', 'service_type', 'duration', 'instructor')
	list_filter = ('name', 'service_type', 'date', 'instructor')
	#search_fields = ('name',)
	raw_id_fields = ('name',)
	ordering = ['date', 'time']
	#inlines = [PostPictureInline,]


admin.site.register(Lesson, LeassonAdmin)