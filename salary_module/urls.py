from django.urls import path

from . import views     # it means - 'from all import views'

urlpatterns = [
    path('', views.calculator, name='calculator'),

]
