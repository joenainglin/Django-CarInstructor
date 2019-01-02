from django import template
register = template.Library()
from django.contrib.auth.models import User

from ..models import *
import requests


@register.simple_tag
def totalavailablejobs():
    return  Lesson.objects.filter(instructor__isnull=True).count()

@register.simple_tag
def instructorjobs():
    jobs =  Lesson.objects.filter(instructor=request.user.profile).count()

    return{'jobs':jobs,}