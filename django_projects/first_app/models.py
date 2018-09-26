from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
"""
class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city= 'Chennai')
"""

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=50, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank = True)

    transport = models.IntegerField(default=0)
    food = models.IntegerField(default=0)
    rent = models.IntegerField(default=0)
    shopping = models.IntegerField(default=0)
    misc = models.IntegerField(default=0)
    cmp_exp = models.IntegerField(default=0)

    def get_compute(self):
        #self.fields['cmp_exp'].widget.attrs['readonly'] = True
        self.cmp_exp  = (self.transport + self.food + self.rent + self.shopping + self.misc)
        return self.user.cmp_exp

    def __str__(self):
        return self.user.username

    #CREATING USER_PROFILE
    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)
