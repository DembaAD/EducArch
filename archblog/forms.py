#from django.contrib.auth.models import User
from django import forms
#from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from django.contrib.auth import get_user_model
from .models import Etudiant, Document, Article, Question, Professeur,Reponse


class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['sujet', 'question']
	
class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['auteur','contenu']

class ArchiveForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = ['description','document']

class UploadFileForm(forms.Form):
	title = forms.CharField(max_length=50)
	file = forms.FileField()

class ReponseForm(forms.Form):
	class Meta:
		model = Reponse
		fields = ['Question','Réponse:']