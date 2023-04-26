from django.db import models

# Create your models here.
class Cour (models.Model):
    nom = models.CharField(max_length=128)
    titre = models.CharField(max_length=128, blank= True, default='bon à savoir')
    contenue = models.TextField|()
    fichier = models.FileField(upload_to='document/')
    

class epreuve (models.Model):
    nom = models.CharField(max_length=128)
    titre = models.CharField(max_length=128, blank= True, default='bon à savoir')
    fichier = models.FileField(upload_to='document/')
    
    
class citations (models.Model):
    contenue = models.CharField(max_length=128)
    auteur = models.CharField(max_length=128, blank= True, default='anonyme')
    

class citations (models.Model):
    nom = models.CharField(max_length=128)
    niveau = models.CharField(max_length=128)
    telephone = models.IntegerField(max_length=15)
    matiere = models.CharField(max_length=200)
    pays = models.CharField(max_length=128)
    ville = models.CharField(max_length=128)
    quatier = models.CharField(max_length=128)
    salaire = models.IntegerField(max_length=128, default=0)
    

class eleve (models.Model):
    nom = models.CharField(max_length=128)
    telephone = models.IntegerField(max_length=15)
    classe = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    filiere = models.CharField(max_length=128)
    pays = models.CharField(max_length=128)
    ville = models.CharField(max_length=128)
    quatier = models.CharField(max_length=128)
    
class preoccupation (models.Model):
    auteur = models.CharField(max_length=128, blank= True, default='anonyme')
    contenue = models.CharField(max_length=128)
    fichier = models.FileField(upload_to='document/', blank=True,)
    
    
  