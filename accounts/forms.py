from django import forms
from django.contrib.auth.models import User
from .models import *

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', )
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email    

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserType(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('grouptype', 'phone' )


class UserEditForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('email',)


class UserAddress(forms.ModelForm):
    
    class Meta:
        model = LearnerAddress
        fields = ('street_no', 'street_name','zipcode','city', 'state')

class UserAddressEdit(forms.ModelForm):
    
    class Meta:
        model = LearnerAddress
        fields = ('street_no', 'street_name','zipcode','city', 'state')



class UserQualification(forms.ModelForm):
    
    class Meta:
        model = InstructorQualification
        #fields = ('grouptype', )
        fields = ('title', 'year','description',)



class UserQualificationEditForm(forms.ModelForm):
    
    class Meta:
        model = InstructorQualification
        #fields = ('grouptype', )
        fields = ('title', 'year','description',)
