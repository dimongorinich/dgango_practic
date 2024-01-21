from django import forms
from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from django.urls import path

from .models import Service, Category, SubCategory


# Register your models here.

@admin.action(description="Archive products")
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)


@admin.action(description="Unarchive products")
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    actions = [
        mark_archived,
        mark_unarchived,
    ]

    list_display = "pk", "name", "description_short", "preview", "archived"
    list_display_links = "pk", "name",
    fieldsets = [
        (None, {
            "fields": ("name", "description", "preview"),
        }),
        ("Extra options", {
            "fields": ("archived",),
            "classes": ("collapse",),
            "description": "Extra options. Field 'archived' is for soft delete",
        })
    ]

    def description_short(self, obj: Service) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + "..."


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "name_category", "preview"
    list_display_links = "name_category",


@admin.register(SubCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "name_subcategory", "preview"
    list_display_links = "name_subcategory",
