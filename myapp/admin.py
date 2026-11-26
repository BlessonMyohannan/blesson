
from django.contrib import admin
from .models import Student,Department
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=(
        "name",
        "age",
        "email"
    )

    search_fields=(
        "name",
        "age"
    )

    ordering=("id",)

admin.site.register(Department)