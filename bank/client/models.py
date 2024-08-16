from django.db import models



class Client(models.Model):
    first = models.CharField(max_length=255)
    nom = models.TextField()
    prenom = models.TextField()
    adresse = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    num_tel = models.PositiveIntegerField(null=True)
    genre = models.TextField(max_length=266, blank=True, null=True)
    nationalité = models.TextField(max_length=266, blank=True, null=True)
    profession = models.TextField(max_length=266, blank=True, null=True)
    statut_mat = models.TextField(max_length=266, blank=True, null=True)
    nbr_per = models.PositiveIntegerField(null=True)
    revenue_annuel = models.FloatField(null=True)
    date_naissance = models.DateField()
    
    


    def __str__(self):
        return self.nom
    

    class Meta:
        ordering = ['-date_naissance']

class Genre(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Nationalité(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Statut_mat(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Nbr_per(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


