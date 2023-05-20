from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.URLField(max_length=256, blank=True, null=True,
                            default='https://pic.616pic.com/ys_img/00/04/60/DToXBfxigM.jpg')
    # openid = models.CharField(default="", max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.user)

# from django.db import models

# # Create your models here.


# class Users(models.Model):
#     username = models.CharField(max_length=30)
#     photo = models.URLField(max_length=256, blank=True)
#     openid = models.CharField(default="", max_length=50, blank=True, null=True)
