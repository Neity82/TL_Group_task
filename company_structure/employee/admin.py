from django.contrib import admin

from employee.models import Position, Department, Employee


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("id", "title",)
    list_display_links = ("id", "title",)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "parent",)
    list_display_links = ("id", "title",)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "position", "department", "date", "is_chief",)
    list_display_links = ("id", "full_name",)
    list_filter = ("position", "department",)
    list_editable = ("is_chief",)
