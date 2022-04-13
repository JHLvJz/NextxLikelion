from django.shortcuts import render, redirect
from .models import Post #models.py에 내가 만들어둔 Post라는 class를 import
from datetime import datetime
# Create your views here.
#home이라는 함수는 request를 매개변수로 받아서,
#posts라는 변수에 potst라는 class에 있는 내용물을 다 담아주고
#home.html에 posts를 'posts'라는 값으로 딕셔너리로 넘겨준다 - 근데 왜 request가 있을깡

def home(request): #Q매개변수에 request넣는 거 원리 이해하기
    posts = Post.objects.all().order_by('deadline')#models.py에 만들어둔 Post라는 class에 접근해서 모든 내용물 가져오기
    # for post in posts:
    #     d_day = Post.deadline - datetime.date(datetime.now())
    #     post.dday = d_day.days
    return render(request, 'home.html', {'posts': posts,}) #Q return방식 이해하기 -> A: render함수를 사용해 반환한다-> 여기에 home.html이라는 목적지와, 전달할 이름과 변수를 딕셔너리로 지정
    #render함수 참고: https://free-eunb.tistory.com/38

def new(request):
    if request.method == 'POST': #Q요거 POST는 뭘까요, request.method랑
        Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline'],
        )
    return render(request, 'new.html')

def detail(request, post_pk): #Q이 함수 너무 어려움
    post = Post.objects.get(pk=post_pk)

    return render(request, 'detail.html', {'post': post})

def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline'],
        )
        return redirect('detail', post_pk)

    return render(request, 'edit.html', {'post': post})

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')
