from django.db import models

# Create your models here.


class Jobs(models.Model):
    name = models.CharField(max_length=30)
    employer = models.CharField(
        max_length=30, blank=True, null=True, default='')
    tag = models.CharField(max_length=30, blank=True, null=True, default='')
    address = models.TextField(default='')
    content = models.TextField(default='')
    require = models.TextField(default='')
    wage = models.CharField(max_length=30, blank=True, null=True, default='')
    experience = models.CharField(
        max_length=10, blank=True, null=True, default='')
    academic = models.CharField(
        max_length=10, blank=True, null=True, default='')
