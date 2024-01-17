from django.urls import path

from .views import ServiceDetailsView


app_name = "apiservice"

urlpatterns = [
    path("service/<int:pk>/", ServiceDetailsView.as_view(), name="service-detail")
]
