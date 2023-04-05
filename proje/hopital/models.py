from django.db import models

# Create your models here.
class Patient(models.Model):
    nom = models.CharField(max_length=100)
    date_Naissance = models.DateField()
    malade = models.BooleanField(default=True)

    def __str__(self):
        return self.nom