from django.urls import path
from .views import applicant_form, success, home

urlpatterns = [
    path('', home, name='home'),
    path('apply/', applicant_form, name='applicant_form'),
    path('success/', success, name='success'),
]