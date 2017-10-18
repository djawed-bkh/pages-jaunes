from django.db import models
from django.contrib.auth.models import User
HOR=(('sa','samedi'),
('di','dimanche'),
('lu','lundi'),
('ma','mardi'),
)
class Entreprise(models.Model):
    nom = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    titre=models.CharField(max_length=255)
    registre_de_commerce=models.CharField(max_length=255)
    description= models.TextField()
    horaires=models.ManyToManyField('entreprises.Horaires')
    def __str__(self):
        return self.nom
    
class Telephone(models.Model):
    numero =models.CharField(max_length=255)
    entreprise=models.ForeignKey(Entreprise)
class Adresse(models.Model):
    adresse=models.CharField(max_length=255)
    entreprise=models.ForeignKey(Entreprise)
    ville=models.CharField(max_length=255)
    code_postal=models.SmallIntegerField(default=31000)
class Horaires(models.Model):
    jour=models.CharField(max_length=3,choices=HOR)
    ouverture=models.TimeField()
    fermeture=models.TimeField()
class Profil(models.Model):
    utilisateur=models.OneToOneField(User)
    remarque=models.TextField(blank=True,null=True)
