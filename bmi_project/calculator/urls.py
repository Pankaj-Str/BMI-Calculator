from django.urls import path
from . import views

urlpatterns = [
    path('calculate_bmi/', views.calculate_bmi, name='calculate_bmi'),
    path('bmi_results/', views.bmi_results, name='bmi_results'),
]
