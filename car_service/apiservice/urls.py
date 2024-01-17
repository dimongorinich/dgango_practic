from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (ServiceDetailsView,
                    ServiceViewSet,
                    )

app_name = "apiservice"


urlpatterns = [
    path("service/<int:pk>/", ServiceDetailsView.as_view(), name="service-detail"),
    path("api/service/", ServiceViewSet.as_view(), name="api-service"),
]
