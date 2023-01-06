from django.urls import path, include
from django.conf.urls import url
from . import views

app_name='archblog'
urlpatterns = [
	path('', views.index , name='index'),
	path('etudiant/', views.student, name='etudiant'),
	path('professeur/', views.teacher, name='profs'),
	path('enregistrement/', views.SignUp.as_view(),name='signup'),
	path('archives/', views.contributions, name='archive'),
	path('article/', views.article_upload, name='article'),
	path('question/', views.questions, name='question'),
	path('upload/', views.model_form_upload, name='upload'),
	path('question_pose/', views.profreponse, name='questions'),
	path('reponse/', views.ReponseCreate.as_view(), name='reponse'),
	path('articles/', views.articles_online, name='articles')

	]