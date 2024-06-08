from django.contrib import admin
from .models import  Applicant

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email')

