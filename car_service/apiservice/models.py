from django.db import models
from django.urls import reverse


# Create your models here.
def service_preview_directory_path(instance: "Service", filename: str) -> str:
    return "services/service_{name}/preview/{filename}".format(
        name=instance.name,
        filename=filename,
    )


def subcategory_preview_directory_path(instance: "SubCategory", filename: str) -> str:
    return "services/service_{name}/preview/{filename}".format(
        name=instance.name_subcategory,
        filename=filename,
    )


def category_preview_directory_path(instance: "Category", filename: str) -> str:
    return "services/service_{name}/preview/{filename}".format(
        name=instance.name_category,
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


class SubCategory(models.Model):
    services = models.ManyToManyField(Service, related_name="subcategory")
    name_subcategory = models.CharField(max_length=100, unique=True)
    preview = models.ImageField(null=False, blank=False, upload_to=subcategory_preview_directory_path)

    def __str__(self):
        return f"{self.name_subcategory}"


class Category(models.Model):
    subcategory = models.ManyToManyField(SubCategory, related_name="category")
    name_category = models.CharField(max_length=100, unique=True)
    preview = models.ImageField(null=False, blank=False, upload_to=category_preview_directory_path)

    def __str__(self):
        return f"{self.name_category}"
