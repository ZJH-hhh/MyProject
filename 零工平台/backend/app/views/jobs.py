from django.shortcuts import render

# Create your views here.
# books/views.py
from rest_framework import viewsets

from app.models.jobs import Jobs
from app.serializer import JobsSerializer


class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
