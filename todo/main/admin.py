from django.contrib import admin

# Register your models here.
from .models import Task
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "category", "user",)
    list_display_links = ("title", )
    search_fields = ("title", "created", "complete",)
    list_filter = ("complete", "category",)
    
from .models import Category
admin.site.register(Category)