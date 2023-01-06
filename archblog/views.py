import os
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django import forms
from django.template.backends.utils import csrf_input_lazy, csrf_token_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ArticleForm, UploadFileForm, ReponseForm,ArchiveForm, QuestionForm
from .models import Etudiant, Question, Reponse, Article


class ReponseCreate(CreateView):
    model = Reponse
    fields = ['question','text']
        
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
def contributions(request):
    path = settings.MEDIA_ROOT
    document_list = os.listdir(path + '')
    context = {'documents': document_list}
    return render(request,'archblog/iindex.html', context)
@login_required
def article_upload(request):
    form = ArticleForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'archblog/article.html')
        else:
            form = ArticleForm()
    return render(request, 'archblog/article.html', {
        'form': form
        })
@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = ArchiveForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'archblog/archive.html')
    else:
        form = ArchiveForm()
    return render(request, 'archblog/archive.html', {
        'form': form
        })
@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url')
        else:
            form = UploadFileForm()
        return render(request, '/archblog/archive/', {'form': form})
def articles_online(request):
    all_articles = Article.objects.all()
    context = {
        'tous_articles': all_articles
    }
    return render(request,'archblog/articles.html', locals())
def profreponse(request):
    all_questions = Question.objects.all()
    template = loader.get_template('archblog/reponse.html')
    context = {
        'all_questions': all_questions,
    }
    form = ReponseForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request,'archblog/reponse.html', locals())
    return render(request, 'archblog/reponse.html', context)
@login_required
def questions(request):
    template = loader.get_template('archblog/question.html')
    form = QuestionForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request,'archblog/question.html')
    return HttpResponse(template.render(request=request))

def index(request):
    template = loader.get_template('archblog/index.html')
    return HttpResponse(template.render(request=request))
def teacher(request):
    template = loader.get_template('archblog/teacher.html')
    return HttpResponse(template.render(request=request))
def student(request):
    template = loader.get_template('archblog/student.html')
    return HttpResponse(template.render(request=request))
def archive(request):
    template = loader.get_template('archblog/archive.html')
    return HttpResponse(template.render(request=request))
