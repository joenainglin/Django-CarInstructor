from django import forms
from django.contrib.auth.models import User
from .models import *

class CreateLessonForm(forms.ModelForm):
    
    class Meta:
        model = Lesson
        fields = ( 'service_type', 'date', 'time', 'duration', )
        widgets = {'date': forms.DateInput(format=('%d%m%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}), 
        			'time': forms.TimeInput(format=('%H:%M'), attrs={'class':'form-control', 'type':'time'})}
		
class AcceptLeassonForm(forms.ModelForm):
    
    class Meta:
        model = Lesson
        fields = ( 'instructor',)
        

