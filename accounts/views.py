from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import *
from .models import *
from leasson.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
from django.contrib import messages





def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            
            login(request, new_user)
            return redirect( '/accounts/usertype')
           # return render(request,
                        #  'accounts/dashboard.html',
                         # {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'registration/register.html',
                  {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, '/registration/login.html', {'form': form})




@login_required
def profile(request): 
    qualification = InstructorQualification.objects.filter(author = request.user)
    useraddress = LearnerAddress.objects.filter(owner = request.user)  
    return render(request, 'accounts/profile.html', {'qualification':qualification,'useraddress':useraddress,})



@login_required
def logout(request):
    logout(request)      
    return render(request, 'accounts/dashboard.html', {'section':logout})


@login_required
def usertype(request):   
    if request.method == "POST":
        form = UserType(data=request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post added successfully')
            if request.user.profile.grouptype == 'Learner':
                return redirect( '/accounts/useraddress')
            if request.user.profile.grouptype == 'Instructor':
                return redirect( '/accounts/userqualification')
          #form = CreateLessonForm()
        else:
          messages.error(request, 'Error adding new post')
    else:
        form = UserType()   
    return render(request, 'accounts/UserType.html',{'form': form, } )

@login_required
def userprofileedit(request):   
    if request.method == "POST":
        userprofileform = UserEditForm(request.POST, instance=request.user)
        if userprofileform.is_valid():
            userprofileform.save()
            messages.success(request, 'Post added successfully')
            return redirect('/accounts/profile')
        else:
          messages.error(request, 'Error adding new post')
    else:
        userprofileform = UserEditForm()
    return render(request, 'accounts/UserProfileEdit.html',{'userprofileform': userprofileform, } )



@login_required
def useraddress(request):   
    if request.method == "POST":
        form = UserAddress( request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            messages.success(request, 'Post added successfully')
            return redirect('/accounts/profile')
            #return redirect( '/accounts/userqualification')
          #form = CreateLessonForm()
        else:
          messages.error(request, 'Error adding new post')
    else:
        form = UserAddress()   
    return render(request, 'accounts/UserAddress.html',{'form': form, } )



@login_required
def useraddressedit(request):   
    if request.method == "POST":
        useraddresseditform = UserAddressEdit(request.POST, instance=request.user)
        if useraddresseditform.is_valid():
            useraddresseditform.save()
            messages.success(request, 'Post added successfully')
            return redirect('/accounts/profile')
        else:
          messages.error(request, 'Error adding new post')
    else:
        useraddresseditform = UserAddressEdit()
    return render(request, 'accounts/UserAddressEdit.html',{'useraddresseditform': useraddresseditform, } )





@login_required
def userqualification(request): 

    if request.method == "POST":
        form = UserQualification( request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post added successfully')
            return redirect('/accounts/profile')
        else:
          messages.error(request, 'Error adding new post')
    else:
        form = UserQualification()   
    return render(request, 'accounts/UserQualification.html',{'form': form, } )




def userqualificationedit(request, slug):
    object_list = get_object_or_404(InstructorQualification, slug=slug)
    form = UserQualificationEditForm( request.POST, request.FILES)
    if request.method == 'POST':
        
        form = UserQualificationEditForm( instance=request.user,
                                    data=request.POST,
                                    files=request.FILES)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

    return render(request, 'accounts/UserQualificationEdit.html',{'object_list': object_list, } )


def getuserprofile(request, username):
    userprofile = User.objects.get(username=username)
    return render(request, 'accounts/GetProfile.html', {"userprofile":userprofile})