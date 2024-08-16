from django.db import models



class Utilisateur(models.Model):
    ident = models.CharField(max_length=255)
    nom = models.TextField()
    prenom = models.TextField()
    email = models.EmailField(max_length=254, unique=True)
    num_tel = models.PositiveIntegerField(null=True)
    genre = models.TextField(max_length=266, blank=True, null=True)
    depart = models.TextField(max_length=266, blank=True, null=True)
    salaire = models.FloatField(null=True)
    date_naissance = models.DateField()
    date_recrut = models.DateField()
    
    


    def __str__(self):
        return self.nom
    

    class Meta:
        ordering = ['-date_recrut']

class Genre(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Depart(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name



