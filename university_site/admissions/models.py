from django.db import models

class Applicant(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
