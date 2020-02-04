from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


urlpatterns = [
    path('employee/', views.EmployeeList),
    path('employee/<int:pk>/', views.EmployeeDetail),
]
