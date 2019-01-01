from django import template
register = template.Library()


from ..models import *
import requests


@register.simple_tag
def totalavailablejobs():
    return  Lesson.objects.filter(instructor__isnull=True).count()

@register.simple_tag
def instructorjobs():
    jobs =  Lesson.objects.filter(instructor=instructor).count()
    return{'jobs':jobs,}