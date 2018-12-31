from django.contrib import admin
from .models import *
# Register your models here.
from .forms import *



admin.site.register(Profile)

admin.site.register(InstructorQualification)
admin.site.register(LearnerAddress)
