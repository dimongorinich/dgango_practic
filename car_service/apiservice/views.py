from rest_framework.generics import ListCreateAPIView

from django.views.generic import DetailView
from rest_framework.viewsets import ModelViewSet

from .models import Service
from .serializers import ServiceSerializer


# Create your views here.


class ServiceDetailsView(DetailView):
    template_name = "apiservice/service-details.html"
    model = Service
    context_object_name = "service"


# class ServiceViewSet(ListCreateAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer

class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
