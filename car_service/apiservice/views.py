from django.shortcuts import render
from django.views.generic import DetailView

from .models import Service


# Create your views here.
class ServiceDetailsView(DetailView):
    template_name = "apiservice/service-details.html"
    model = Service
    context_object_name = "service"
