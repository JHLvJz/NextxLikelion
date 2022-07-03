from django.shortcuts import render, redirect
from .models import Article, Comment, Like, Scrap

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from urllib import response
from django.http import HttpResponse
import json

# Create your views here.
def home(request):
    articles = Article.objects.all()
    return render(request, 'home.html', {'articles':articles})

#------기본CRUD------

@login_required(login_url='/registration/login')
def new(request):
    if request.method == 'POST':
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user
        )
        return redirect('detail', new_article.pk)
        #redirect함수에는 url name을 넣어줬던 거 기억해랑
    return render(request, 'new.html')

@login_required(login_url='/registration/login')
def detail(request, article_pk):
    article = Article.objects.get(pk = article_pk)
    #로그인한 유저가 좋아요를 눌렀는지 따로 확인
    isMeLiked = Like.objects.filter(
        author = request.user
    ).count() 
    #로그인한 유저가 찜하기를 눌렀는지 따로 확인
    isMeScrapped = Scrap.objects.filter(
        author = request.user
    ).count()

    #해당 게시물의 디테일 창에서 댓글 구현
    if request.method == 'POST':
        comment = Comment.objects.create(
            article = article,
            content = request.POST['content'],
            author = request.user
        )
        return redirect('detail', article_pk)
    
    return render(request, 'detail.html', {'article':article, 'isMeLiked': isMeLiked, 'isMeScrapped': isMeScrapped})

def edit(request, article_pk):
    article = Article.objects.get(pk = article_pk)
    if request.method == 'POST':
        Article.objects.filter(pk = article_pk).update(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('detail', article_pk)
    return render(request, 'edit.html', {'article', article})

def delete(request, article_pk):
    article = Article.objects.get(pk = article_pk)
    article.delete()
    return redirect('home')

def delete_comment(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    comment.delete()
    return redirect('detail', article_pk)

#------유저로그인------
#복습참고(장고공식문서: https://docs.djangoproject.com/en/4.0/topics/auth/default/ ) 

def signup(request):
    if request.method == 'POST':
        found_user = User.objects.filter(username = request.POST['username'])
        #같은 이름의 유저 1명 이상이면
        if len(found_user) > 0 :
            error = '이미 존재하는 닉네임입니다.'
            return render(request, 'registration/signup.html', {'error':error})
        #같은 이름 유저 없으면
        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
        auth.login(
            request,
            new_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect('home')
    return render(request, 'registration/signup.html')

def login(request):
    if request.method == 'POST':
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if(found_user is None):
            error = '아이디 또는 비밀번호가 틀렸습니다'
            return render(request, 'registration/login.html', {'error':error})
        auth.login(
            request,
            found_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect(request.GET.get('next', '/'))
    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

#------좋아요 기능------
@csrf_exempt
def like(request):
    isLiked = False

    if request.method == "POST":
        request_body = json.loads(request.body)
        article_pk = request_body["article_pk"]
        
        #Like의 object 중 해당 좋아요와 연결되어있는 게시물, 유저를 조건으로 하여 하나의 객체를 existing_like에 담음
        existing_like = Like.objects.filter(
            article = Article.objects.get(pk=article_pk),
            author = request.user
        ) 

        #취소 기능
        if existing_like.count() > 0 :
            existing_like.delete()

        #생성 기능
        else:
            Like.objects.create(
                article = Article.objects.get(pk=article_pk),
                author = request.user
            )
            isLiked = True

    article_likes = Like.objects.filter(
        article = Article.objects.get(pk=article_pk)
    )
    response = {
        'like_count': article_likes.count(), 'isLiked': isLiked
    }

    return HttpResponse(json.dumps(response))

#------스크랩 기능------
@csrf_exempt
def scrap(request):
    isScrapped = False

    if request.method == 'POST':
        request_body = json.loads(request.body)
        article_pk = request_body["article_pk"]

        existing_scrap = Scrap.objects.filter(
            article = Article.objects.get(pk=article_pk),
            author = request.user
        )

        #취소 
        if existing_scrap.count() > 0 :
            existing_scrap.delete()

        #생성
        else:
            Scrap.objects.create(
                article = Article.objects.get(pk=article_pk),
                author = request.user
            )
            isScrapped = True
        
        article_scraps = Scrap.objects.filter(
            article = Article.objects.get(pk=article_pk)
        )

        response = {
            'scrap_count': article_scraps.count(), 'isScrapped' : isScrapped
        }

        return HttpResponse(json.dumps(response))

#------Mypage------
def mypage(request):
    liked_posts = Like.objects.filter(author = request.user)
    scrapped_posts = Scrap.objects.filter(author = request.user)
    return render(request, 'mypage.html', {'liked_posts':liked_posts, 'scrapped_posts':scrapped_posts,})
