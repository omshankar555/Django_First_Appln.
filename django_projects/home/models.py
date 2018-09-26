from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Post(models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #reply = models.CharField(max_length=500, default= 'null')

    def __str__(self):
        return self.user.username

    #CREATING USER_PROFILE
    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = Post.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)

"""
class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.remove(new_friend)
"""