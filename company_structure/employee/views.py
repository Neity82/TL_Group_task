import json
from typing import List, Tuple, Dict

from django.db.models import QuerySet
from django.http import HttpResponse
from django.views import generic

from employee.models import Department, Employee


class IndexView(generic.ListView):
    template_name = "employee/index.html"
    context_object_name = "departments_list"

    def get_queryset(self) -> QuerySet[Department]:
        queryset: QuerySet[Department] = Department.objects.filter(parent=None)
        return queryset

    def post(self, request, *args, **kwargs) -> HttpResponse:
        """
        Обработка POST запроса, полученного с помощью AJAX.
        """

        dep_id: str = str(request.POST["dep_id"])
        employees: List[Tuple[str, str]] = list(
            Employee.objects.select_related("Position")
                .values_list("full_name", "position__title")
                .filter(department__id=dep_id)
        )

        response_data: Dict[str, List[Tuple[str, str]]] = {
            "employees": employees
        }

        return HttpResponse(
            json.dumps(response_data, default=str), content_type="application/json"
        )
