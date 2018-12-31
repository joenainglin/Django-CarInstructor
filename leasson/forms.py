from django import forms
from django.contrib.auth.models import User
from .models import *

class CreateLessonForm(forms.ModelForm):
    
    class Meta:
        model = Lesson
        fields = ( 'service_type', 'date', 'time', 'duration', )

class AcceptLeassonForm(forms.ModelForm):
    
    class Meta:
        model = Lesson
        fields = ( 'instructor',)
        

