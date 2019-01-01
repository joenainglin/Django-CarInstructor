from django.contrib import admin
from .models import *
# Register your models here.
from .forms import *

class LearnerAddressAdmin(admin.ModelAdmin):
	list_display = ('owner','street_no', 'street_name', 'zipcode', 'city', 'state', 'slug')
	list_filter = ('owner', 'zipcode', 'city', 'state')
	#search_fields = ('name',)
	raw_id_fields = ('owner',)
	ordering = ['owner',]
	#inlines = [PostPictureInline,]

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user','grouptype', )
	list_filter = ('user', 'grouptype',)
	#search_fields = ('name',)
	raw_id_fields = ('user',)
	ordering = ['user',]
	#inlines = [PostPictureInline,]


class InstructorQualificationAdmin(admin.ModelAdmin):
	list_display = ('author','title','year', 'description', 'slug')
	list_filter = ('author', 'year',)
	#search_fields = ('name',)
	raw_id_fields = ('author',)
	ordering = ['author',]
	#inlines = [PostPictureInline,]


admin.site.register(Profile, ProfileAdmin)

admin.site.register(InstructorQualification, InstructorQualificationAdmin)
admin.site.register(LearnerAddress, LearnerAddressAdmin)
