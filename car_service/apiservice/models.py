from django.db import models
from django.urls import reverse


# Create your models here.
def service_preview_directory_path(instance: "Service", filename: str) -> str:
    return "services/service_{name}/preview/{filename}".format(
        name=instance.name,
        filename=filename,
    )


class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    archived = models.BooleanField(default=False)
    preview = models.ImageField(null=True, blank=False, upload_to=service_preview_directory_path)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('apiservice:service-detail', kwargs={'pk': self.pk})
