from datetime import datetime
import random

from django.db import models
from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _


class Position(models.Model):
    """Модель: Должность"""

    title = models.CharField(
        verbose_name=_("title"),
        max_length=100,
    )

    class Neta:
        db_table = "positions"
        verbose_name = _("position")
        verbose_name_plural = _("positions")
        ordering = ["title"]

    def __str__(self) -> str:
        return getattr(self, "title")


class Department(models.Model):
    """Модель: Подразделение (отдел)"""

    SEP = " / "

    title = models.CharField(
        verbose_name=_("title"),
        max_length=100,
    )
    parent = models.ForeignKey(
        "Department",
        on_delete=models.CASCADE,
        verbose_name=_("parent"),
        related_name="child",
        null=True,
        blank=True,
        default=None,
    )

    objects = models.Manager()

    class Meta:
        db_table = "departments"
        verbose_name = _("department")
        verbose_name_plural = _("departments")
        ordering = ["id"]

    def __str__(self) -> str:
        return self.get_department_recur()

    def get_department_recur(self) -> str:
        """Рекурсивно получаем названия подразделений и их родителей"""

        title = getattr(self, "title")
        parent = getattr(self, "parent")
        return f"{parent.get_department_recur()}{self.SEP}{title}" if parent else title


class Employee(models.Model):
    """Модель: Сотрудник"""

    full_name = models.CharField(
        verbose_name=_("full name"),
        max_length=100,
    )
    position = models.ForeignKey(
        "Position",
        on_delete=models.CASCADE,
        related_name="employee",
        verbose_name=_("position"),
    )
    date = models.DateField(
        verbose_name=_("date of employment"),
    )
    salary = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name=_("salary"),
    )
    department = models.ForeignKey(
        "Department",
        on_delete=models.CASCADE,
        related_name="employee",
        verbose_name=_("department"),
    )

    is_chief = models.BooleanField(
        default=False,
        verbose_name=_("is chief")
    )

    objects = models.Manager()

    class Meta:
        db_table = "employees"
        verbose_name = _("employee")
        verbose_name_plural = _("employees")
        ordering = ["-is_chief", "full_name"]

    def __str__(self):
        return getattr(self, "full_name")

