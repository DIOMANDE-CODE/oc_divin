from django.db import models

# Create your models here.

class Prospects(models.Model):
    email=models.EmailField(verbose_name="Email", unique=True,max_length=60)
    nom=models.CharField(verbose_name="Nom", max_length=255)
    prenom=models.CharField(verbose_name="prenom",max_length=255)
    numero1=models.IntegerField(verbose_name="Numéro de téléphone")
    numero2=models.IntegerField(verbose_name="Numéro whatsapp")
    lieu=models.CharField(verbose_name="lieu de naissance",max_length=255)
    sexe=models.CharField(verbose_name="Sexe",max_length=255)
    filiere=models.CharField(verbose_name="Filière",max_length=255)
    diplome=models.CharField(verbose_name="Diplôme",max_length=255)
    date=models.DateField()

    REQUIRED_FIELDS='__all__'

    def __str__(self):
        return self.email

class Delegate(models.Model):
    delegue=models.ForeignKey(Prospects,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)

