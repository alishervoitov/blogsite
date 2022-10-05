from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.http.response import JsonResponse, HttpResponse
from .models import Article, Author, Person, User
import json
from .forms import LoginForm,RegistrationForm
from .decorators import not_logged


def author(request, id):
    author = Author.objects.get(id=id)
    return render(
        request=request,
        template_name='blog/author.html',
        context={
            'author': author
        }
    )


def articles(request):
    articles = Article.objects.all()
    authors = Author.objects.all()
    return render(request=request,
                  template_name='blog/index.html',
                  context={
                      'articles': articles,
                      'authors': authors
                  }
                  )

def article_detail(request, id):
    article = Article.objects.get(id=id)

    return render(request=request,
                  template_name='blog/article_detail.html',
                  context={
                      'article': article,

                  }
                  )

def comment(request,id):
    if request.method == 'POST':
        if request.user.username:
            data = json.loads(request.body)
            print(data)
            comment = data.get('comment',None)
            person = Person.objects.get(user=request.user)
            article = Article.objects.get(id=id)
            if comment:
                article.setcomment(comment=comment, person=person)
                return HttpResponse(status=201)

def reaction(request, id, react):
    article = Article.objects.get(id=id)
    if request.user.username:
        person = Person.objects.get(user=request.user)
        article.setreaction(react=react, person=person)
    return JsonResponse({
        'likes':article.likes,
        'dislikes':article.dislikes,
    })

@not_logged
def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.data.get('username')
            password = login_form.data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('articles')

    return render(
        request=request,
        template_name='blog/login.html',
        context={
        }
    )

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')

@not_logged
def registration(request):
    error_user = None
    error_confirm = None
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            first_name = reg_form.data.get('first_name')
            last_name = reg_form.data.get('last_name')
            username = reg_form.data.get('username')
            email = reg_form.data.get('email')
            password = reg_form.data.get('password')
            password1 = reg_form.data.get('password1')
            res = User.objects.filter(username=username)
            if password == password1 and len(res) == 0:
                user = User.objects.create(
                    username = username,
                    first_name = first_name,
                    last_name = last_name,
                    password = password
                )
                person = Person.objects.create(user=user)
                login(request,user)
                return redirect('articles')
            else:
                error_user = 'Bu foydalanuvchi nomi band' if len(res)!=0 else None
                error_confirm = 'Parolni to\'g\'ri kiritilganiga ishonch hosil qiling' if password1 != password else None

    return render(request,'blog/registration.html',context={
        'error_user':error_user,
        'error_confirm':error_confirm
    })