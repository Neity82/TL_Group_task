from django import template
from django.db.models import QuerySet

from employee.models import Department

register = template.Library()


@register.simple_tag
def get_departments(dep_id: int) -> QuerySet[Department]:
    """
    Получаем id подразделения и возвращаем queryset
    из всех дочерние подразделения (прямые наследники)
    """

    queryset = Department.objects.filter(parent_id=dep_id)
    return queryset

