from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def home_page(request):
    articles = Article.objects.all()
    return render(request, 'Board/home_page.html', {'articles': articles})
#모델로부터 모든 객체들을 posts에 담아 딕셔너리 형태로 전달
#render함수 원형 1번째 인자=request, 2번째 인자=템플릿, 3번째 인자=context(딕셔너리)

def create_page(request):
    if request.method == 'POST': #POST형태로 클라이언트 요청이 들어오면,
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            viewcount = 0
        )
        return redirect('home_page', new_article.pk)
        #redirect의 함수 원형: redirect(to, permanent=False, *args, **kwargs)
        # 이동할 URL이 첫번째 인자
        # id = 장고에서 모델을 생성할 때 자동으로 증가하며 생성되는 primary-key
        # pk = 데이터베이스의 table에서 고유한 값, 다른 행과 절대 겹치지 않음
    return render(request, 'Board/create_page.html')

def detail_page(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.viewcount += 1
    return render(request, 'Baord/detail_page.html', {"article": article})


def edit_page(request, article_pk):
    article = Article.objects.filter(pk=article_pk)
    if request.method == 'POST':
        article.update(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('detail', article_pk)
    return render(request, 'Board/edit.html', {'article': article[0]})

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('home')


