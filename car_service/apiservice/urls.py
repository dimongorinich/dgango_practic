from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (ServiceDetailsView,
                    ServiceViewSet,
                    )

app_name = "apiservice"

routers = DefaultRouter()
routers.register("services", ServiceViewSet)

urlpatterns = [
    path("service/<int:pk>/", ServiceDetailsView.as_view(), name="service-detail"),
    path("api/", include(routers.urls)),
]
