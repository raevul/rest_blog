from django.db import models

from account.models import MyUser


class UserProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='user_profile')
    avatar = models.ImageField(upload_to='posts', blank=True, null=True)
    bio = models.TextField()

    def __str__(self):
        return self.user.email
    