
# Use datetime if not localizing timezones
import datetime as dt
# Otherwise use timezone
from django.utils import timezone
from django import template
register = template.Library()
from django.contrib.auth.models import User
from django.utils.timesince import timesince
from ..models import *
import requests
from datetime import date

@register.simple_tag
def totalavailablejobs():
    return  Lesson.objects.filter(instructor__isnull=True).count()

@register.simple_tag
def instructorjobs():
    jobs =  Lesson.objects.filter(instructor=request.user.profile).count()

    return{'jobs':jobs,}
@register.filter
def hours_ago(time, hours):
	time = dt.datetime.now() # 8
	delta = dt.timedelta(hours = hours) # 24
	if dt.datetime.now() - time > delta:
		return timesince(time)  # 8

@property
def is_past_due(self):
    return date.today() < self.date