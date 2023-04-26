from django.db import models

# Create your models here.
class Cours (models.Model):
    nom = models.CharField(max_length=128)
    titre = models.CharField(max_length=128, default='bon à savoir')
    contenue = models.TextField(blank=True)
    fichier = models.FileField(upload_to='document/cours/', blank=True)
    

class Epreuves (models.Model):
    nom = models.CharField(max_length=128)
    titre = models.CharField(max_length=128, blank= True, default='bon à savoir')
    contenue = models.TextField(blank=True)
    fichier = models.FileField(upload_to='document/epreuve/', blank=True)
    
    
class Citations (models.Model):
    contenue = models.CharField(max_length=128)
    auteur = models.CharField(max_length=128, blank= True, default='anonyme')
        
    

class Utilisateurs (models.Model):
    # Les champs avec le R à la fin sont les champs destinée au repetiteur uniquement 
    # Les champs avec le E à la fin sont les champs destinée au eleve  uniquement
    # Le reste de champs le sont commun 
    
    nom = models.CharField(max_length=128)
    niveauR = models.CharField(max_length=128)
    filiere = models.CharField(max_length=128)
    telephone = models.IntegerField(max_length=15)
    matiere_dispenserR = models.CharField(max_length=200)
    classeE = models.CharField(max_length=128, choices=['3eme', '2nd','premier','terminal'], default='')
    etablissement = models.CharField(max_length=128, blank=True)
    password = models.CharField(max_length=128)
    salaireR = models.IntegerField(max_length=128, default=0)
    pays = models.CharField(max_length=128)
    ville = models.CharField(max_length=128,)
    quatier = models.CharField(max_length=128)
    role = models.CharField(default='eleve', choices=['eleve','repetiteur'], max_length=128)
    
    
    
class Preoccupation (models.Model):
    auteur = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE)
    contenue = models.CharField(max_length=128)
    fichier = models.FileField(upload_to='document/preoccupation', blank=True,)
    classe = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE)
    

class Reponse (models.Model):
    auteur = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE)
    contenue = models.CharField(max_length=128)
    fichier = models.FileField(upload_to='document/reponse', blank=True,)
    classe = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE)
    poste = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE)
    
class Competition (models.Model):
    auteur = models.CharField(max_length=128)
    contenue = models.CharField(max_length=128)
    fichier = models.FileField(upload_to='document/competition', blank=True,)
    classe = models.CharField(max_length=128, choices=['3eme', '2nd','premier','terminal'], default='')
    date_debut_Competion = models.DateField()
    date_fin_Competion = models.DateField()
    poste = models.ForeignKey(default='MOCTA-EDUCATION', max_length=128)
    
    
class ReponseCompetition (models.Model):
      
    eleve = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE)
    reponse1 = models.TextField()
    reponse2 = models.FileField(upload_to='document/reponse/reponse_competition')
       