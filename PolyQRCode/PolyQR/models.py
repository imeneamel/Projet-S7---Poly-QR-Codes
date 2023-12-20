from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

class Professeur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cours_inscrits = models.ManyToManyField('Cours')

class Promotion(models.Model):
    annee_academique = models.CharField(max_length=4)
    groupe = models.CharField(max_length=10)

class SalleDeClasse(models.Model):
    nom = models.CharField(max_length=50)
    coordonnees_geographiques = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=20)

class Cours(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    professeur_responsable = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    matiere = models.ForeignKey('Matiere', on_delete=models.CASCADE)
    salle = models.ForeignKey(SalleDeClasse, on_delete=models.CASCADE)

class Matiere(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()

class PresenceEtudiant(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    marque_temporelle = models.DateTimeField(auto_now_add=True)
