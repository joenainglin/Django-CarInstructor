from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from accounts.models import *
from django.template.defaultfilters import slugify



# Create your models here.
class Lesson(models.Model):
	SERVICE_TYPE = (
        ('Manual', 'Manual'),
        ('Auto', 'Auto'),
    )

	name = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
	slug = models.SlugField(max_length=140, unique=True, null = False, blank = True)
	service_type = models.CharField(max_length=10, choices=SERVICE_TYPE, default='Auto')
	duration = models.PositiveIntegerField( default=1)
	date = models.DateField(default = timezone.now)
	time = models.TimeField(default = timezone.now)
	instructor = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name ='instructor')
	


        
	def save(self, *args, **kwargs):
		super(Lesson, self).save(*args, **kwargs)
		if not self.slug:
		   	self.slug = slugify(self.id)
		   	self.save()


	def get_absolute_url(self):
		return reverse('leasson:leassondeatil', args=[
												 self.id
			])
	class Meta: 
		ordering = ("-date", "time")

	def __str__(self):
		return 'Booked by {}, and accepted {}'.format(self.name, self.instructor) 