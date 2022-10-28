from django.urls import path
from employee.views import IndexView

app_name = "employee"

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
]
