from django.db import models
from django.db.models.signals import *
#from core.models import UserProfile
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import AbstractUser,User
from django.dispatch import *


class Article(models.Model):
	titre = models.CharField(max_length=100,blank=True)
	auteur = models.CharField(max_length=42)
	contenu = models.TextField(null=True)
	date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
	def __str__(self):
		return self.auteur
class Question(models.Model):
	#auteur = models.OneToOneField(Etudiant, on_delete=models.CASCADE)
	sujet = models.CharField(max_length=255, blank=True)
	question = models.TextField(help_text="Votre question...")
	
	def __str__(self):
		return self.question

class Document(models.Model):
	description = models.CharField(max_length=255, blank=True)
	document = models.FileField(upload_to='archive/')
	upload_at = models.DateTimeField(auto_now_add=True)

class Reponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField('Reponse...', max_length=255)

    def get_absolute_url(self):
    	return reverse('archblog:index')
    def __str__(self):
        return self.text
		
class Etudiant(models.Model):
	
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	nom = models.CharField(max_length=250)
	prenom = models.CharField(max_length=200)
	matricule = models.CharField(max_length=10, unique=True)
	specialite = models.CharField(max_length=200)
	mail = models.EmailField(max_length=1000)
	REQUIRED_FIELDS=[]
	USERNAME_FIELD='matricule'
	is_authenticated=True
	is_anonymous=True
#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, create, **kwargs):
	#if created:
		#Etudiant.objects.create(user=etudiant)
#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, create, **kwargs):
	#instance.etudiant.save()
	def __str__(self):
			return self.nom + ' - ' + self.prenom
class EtudiantReponse(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='quiz_answers')
    reponse = models.ForeignKey(Reponse, on_delete=models.CASCADE, related_name='+')

class Professeur(models.Model):

	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
	nom = models.CharField(max_length=200)
	prenom = models.CharField(max_length=200)
	specialite = models.CharField(max_length=200)
	mail = models.EmailField(max_length=200)
	numero = models.CharField(max_length=12)
#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, create, **kwargs):
	#if created:
		#Professeur.objects.create(user=instance)
#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, create, **kwargs):
	#instance.professeur.save()
	def __str__(self):
			return self.nom + ' - ' + self.prenom