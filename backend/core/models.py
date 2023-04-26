from django.db import models

# Create your models here.
class Cour (models.Model):
    nom = models.CharField(max_length=128)
    titre = models.CharField(max_length=128, blank= True, default='bon à savoir')
    contenue = models.TextField|()
    fichier = models.FileField(upload_to='document/')