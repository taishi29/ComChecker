from django.urls import path
from . import views

urlpatterns = [
    path('company/<int:index>/', views.show_company, name='show_company'),
    path('evaluate/', views.evaluate_company, name='evaluate_company'),
    path('result/', views.show_result, name='show_result'),
]
