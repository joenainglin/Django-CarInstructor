from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import *
from .models import Lesson
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

import datetime
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.contrib import messages

from datetime import datetime, timedelta, time


def home(request): 
    return render(request, 'leasson/HomePage.html', {}) 

@login_required
def dashboard(request): 
    object_list = Lesson.objects.filter(instructor__isnull=True).order_by("-date", "time")
    today = datetime.now().date()
    TodayJob =  Lesson.objects.filter(instructor=request.user.profile, date=today).order_by("-date","time")
    return render(request, 'leasson/dashboard.html', {#'page': page, 
                                                   #'posts': posts, 
                                                  
                                                   'object_list': object_list,
                                                   'TodayJob':TodayJob
                                               
                                       
                                                  }) 



@login_required
def createleasson(request):

    if request.method == "POST":
        form = CreateLessonForm(
                                    request.POST, request.FILES,)

        if form.is_valid():
          #cd = form.cleaned_data
          new_item = form.save(commit=False)
         
          new_item.name = request.user.profile
          

          new_item.save()
          new_item.slug = new_item.id
          new_item.save()
        
          messages.success(request, 'You have successfully book a Lesson!')
          return redirect( '/my_leasson')
          #form = CreateLessonForm()
        else:
          messages.error(request, 'Error')
    else:
        form = CreateLessonForm()
    return render(request, 'leasson/CreatLeasson.html',{'form': form, } )





def leassondeatil(request, id):
  object_list = get_object_or_404(Lesson, id=id)
  useraddress = LearnerAddress.objects.filter( owner=object_list.name.user)

  return render(request, 'leasson/LeassonDeatil.html', {'useraddress':useraddress, 'object_list':object_list})




@login_required
def MyJob(request):
    today = datetime.now().date()
    UserJob =  Lesson.objects.filter(instructor=request.user.profile).order_by("-date","time")
    TodayJob =  Lesson.objects.filter(instructor=request.user.profile, date=today).order_by("-date","time")
    totaljob = UserJob.count()
    return render(request, 'leasson/MyJob.html',{'UserJob': UserJob,'totaljob':totaljob,'today':today, 'TodayJob':TodayJob } )


@login_required
def leasson_delete(request, slug):
    object_list = get_object_or_404(Lesson, slug= slug)
    object_list.delete()
    messages.success(request, "You have successfully deleted a leasson!")
    return redirect( '/my_leasson')

@login_required
def my_leasson(request):
    UserPost = Lesson.objects.filter(name_id=request.user.profile).order_by("-date", "-time")
    totalleasson = UserPost.count()
    #return redirect( '/accounts/dashboard.html')
    return render(request, 'leasson/MyLeasson.html', {'UserPost':UserPost, 'totalleasson':totalleasson})


@login_required
def accept_jobs(request, slug):
   object_list = get_object_or_404(Lesson, slug= slug)
   if request.method == "POST":
        form = AcceptLeassonForm(
                                    request.POST, instance=object_list)

        if form.is_valid():
          #cd = form.cleaned_data
          new_item = form.save(commit=False)
         
          new_item.instructor = request.user.profile

          new_item.save()
          from_email = object_list.instructor.user.email
          reciever_email = object_list.name.user.email
          subject = '{}, You leasson number {} has been accepted!'.format(object_list.name, slug)
          message = '\tLeasson Detail\nName:{}\nLeasson Number:{}\nService type:{}\nDate:{}\nTime:{}\nYour instructor for this leasson:{}'.format(object_list.name, object_list.slug, object_list.service_type, object_list.date, object_list.time, object_list.instructor)
          try:
              send_mail(subject, message,from_email, [reciever_email],fail_silently=False)
              messages.success(request, "Message have been sucessfully send.")
          except BadHeaderError:
              messages.success(request, "Message have fail to send.")
          
          return render(request, 'leasson/AccaptJob.html',{'object_list': object_list,}) 
   else:
        form = AcceptLeassonForm()

   return render(request, 'leasson/LeassonDeatil.html',{'object_list': object_list, 
                                                    'form':form} )


@login_required
def termandcondition(request):
   return render(request, 'leasson/TermAndCondition.html',{} )



@login_required
def cancel_job(request, slug):
   object_list = get_object_or_404(Lesson, slug= slug)
   if request.method == "POST":
        form = AcceptLeassonForm(
                                    request.POST, instance=object_list)

        if form.is_valid():
          #cd = form.cleaned_data
          new_item = form.save(commit=False)
          new_item.instructor = form.cleaned_data.get("new_item.instructor")
     

          new_item.save()
          from_email = settings.EMAIL_HOST
          reciever_email = object_list.name.user.email
          subject = '{}, You leasson number {} has been cancelled!'.format(object_list.name, slug)
          message = '\tLeasson Detail\nName:{}\nLeasson Number:{}\nService type:{}\nDate:{}\nTime:{}\nYour instructor for this leasson:{}'.format(object_list.name, object_list.slug, object_list.service_type, object_list.date, object_list.time, object_list.instructor)
          try:
              send_mail(subject, message,from_email, [reciever_email],fail_silently=False)
              messages.success(request, "Message have been sucessfully send.")
          except BadHeaderError:
              messages.success(request, "Message have fail to send.")
          
          return render(request, 'leasson/AccaptJob.html',{'object_list': object_list,}) 
        
          
         
   else:
        form = AcceptLeassonForm()

   return render(request, 'leasson/LeassonDeatil.html',{'object_list': object_list, 
                                                    'form':form} )
