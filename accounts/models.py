from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify
from django.urls import reverse



#class LearnerAdress(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
 #   street_no = models.CharField( max_length = 100, blank=True,)
#    street_name = models.CharField(max_length=50, blank=True)
#    zipcode = models.CharField( max_length = 5, blank = True)
#    city = models.CharField( max_length = 100, blank = True)
#    state = models.CharField( max_length = 100, blank = True)

#class Qualification(models.Model):
#    title = models.CharField( max_length = 100, blank = True)
#    year = models.CharField( max_length = 100, blank = True)
#    description = models.CharField( max_length = 100, blank = True) 


class InstructorQualification(models.Model):
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    title = models.CharField( max_length = 100, blank = True)
    slug = models.SlugField(max_length=140, unique=True, null = False, blank = True)
    year = models.CharField( max_length = 100, blank = True)
    description = models.CharField( max_length = 500, blank = True) 


        
    def save(self, *args, **kwargs):
        super(InstructorQualification, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.id)
            self.save()
    def __str__(self):
        return self.author.username


class LearnerAddress(models.Model):
    owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=140, unique=True, null = False, blank = True)
    street_no = models.CharField( max_length = 100, blank=True,)
    street_name = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField( max_length = 5, blank = True)
    city = models.CharField( max_length = 100, blank = True)
    state = models.CharField( max_length = 100, blank = True)
        
    def save(self, *args, **kwargs):
        super(LearnerAddress, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.id)
            self.save()

    def __str__(self):
        return '{} Address '.format(self.owner.username)


class Profile(models.Model):
    GROUP_TYPE = (
        ('Learner', 'Learner'),
        ('Instructor', 'Instructor'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(default=None, blank=True, null=True, max_length=10)
    grouptype = models.CharField(max_length=10, choices=GROUP_TYPE, default='Learner')       

    def __str__(self):
        return (self.user.username)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)



    def __str__(self):
        return self.user.username