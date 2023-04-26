from django.db import models

# Create your models here.
class Cours (models.Model):
    nom = models.CharField(max_length=128)
    titre = models.CharField(max_length=128, default='bon à savoir')
    contenue = models.TextField(blank=True)
    fichier = models.FileField(upload_to='document/cours/', blank=True)
    date_publication = models.DateField(null=True)
    

class Epreuves (models.Model):
    nom = models.CharField(max_length=128)
    titre = models.CharField(max_length=128, blank= True, default='bon à savoir')
    contenue = models.TextField(blank=True)
    fichier = models.FileField(upload_to='document/epreuve/', blank=True)
    date_publication = models.DateField(null=True)
    
    
class Citations (models.Model):
    contenue = models.CharField(max_length=128)
    auteur = models.CharField(max_length=128, blank= True, default='anonyme')
    date_publication = models.DateField(null=True)
        
    

class Utilisateurs (models.Model):
    # Les champs avec le R à la fin sont les champs destinée au repetiteur uniquement 
    # Les champs avec le E à la fin sont les champs destinée au eleve  uniquement
    # Le reste de champs le sont commun 
    
    nom = models.CharField(max_length=128)
    niveauR = models.CharField(max_length=128)
    filiere = models.CharField(max_length=128)
    telephone = models.IntegerField()
    matiere_dispenserR = models.CharField(max_length=200)
    classeE = models.CharField(max_length=128, choices=(('3eme','3eme'), ('2nd','2nd'),('premier','premier'),('terminal','terminal')), default='')
    etablissement = models.CharField(max_length=128, blank=True)
    password = models.CharField(max_length=128)
    salaireR = models.IntegerField(default=0)
    pays = models.CharField(max_length=128)
    ville = models.CharField(max_length=128,)
    quatier = models.CharField(max_length=128)
    role = models.CharField(default='eleve', choices=(('eleve','eleve'),('repetiteur','repetiteur')), max_length=128)
    date_inscription = models.DateField(null=True)
    
    
    
    
class Preoccupation (models.Model):
    auteur = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE,related_name='mocta1')
    contenue = models.CharField(max_length=128)
    fichier = models.FileField(upload_to='document/preoccupation', blank=True,)
    classe = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE,related_name='mocta2')
    date_publication = models.DateField(null=True)
    

class Reponse (models.Model):
    auteur = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE)
    contenue = models.CharField(max_length=128)
    fichier = models.FileField(upload_to='document/reponse', blank=True,)
    classe = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE,related_name='mocta3')
    poste = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE,related_name='mocta4')
    date_publication = models.DateField(null=True)
    
class Competition (models.Model):
    auteur = models.CharField(max_length=128)
    contenue = models.CharField(max_length=128)
    fichier = models.FileField(upload_to='document/competition', blank=True,)
    classe = models.CharField(max_length=128, choices=(('3eme','3eme'), ('2nd','2nd'),('premier','premier'),('terminal','terminal')), default='')
    date_debut_Competion = models.DateField()
    date_fin_Competion = models.DateField()
    poste = models.CharField(default='MOCTA-EDUCATION', max_length=128)
    date_publication = models.DateField(null=True)
    
    
class ReponseCompetition (models.Model):
      
    eleve = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE,related_name='mocta5')
    reponse1 = models.TextField()
    reponse2 = models.FileField(upload_to='document/reponse/reponse_competition')
    date_publication = models.DateField(null=True)
       