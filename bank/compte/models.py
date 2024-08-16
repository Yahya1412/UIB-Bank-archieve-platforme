from django.db import models



class Compte(models.Model):
    rib = models.CharField(max_length=255)
    owner = models.TextField()
    type = models.CharField(max_length=266, blank=True, null=True)
    num_compte = models.PositiveIntegerField(null=True)
    solde = models.FloatField(null=True)
    etat = models.CharField(max_length=266, blank=True, null=True)
    date_debut = models.DateField()
    
    


    def __str__(self):
        return self.owner
    

    class Meta:
        ordering = ['-date_debut']

class Type(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Etat(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


