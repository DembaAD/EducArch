from django.contrib import admin
from .models import User,Reponse,Etudiant, EtudiantReponse, Professeur, Article, Question,Document


#admin.site.register(Etudiant)
#admin.site.register(Professeur)
admin.site.register(Article)
admin.site.register(Question)
admin.site.register(Document)
admin.site.register(Reponse)
#admin.site.register(EtudiantReponse)