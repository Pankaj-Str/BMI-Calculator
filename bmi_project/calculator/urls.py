from django.urls import path
from calculator import views

urlpatterns = [
    path('bmi/', views.calculate_bmi, name='calculate_bmi'),
]