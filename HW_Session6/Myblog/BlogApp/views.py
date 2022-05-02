from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def new(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            category = request.POST['category'],
            content = request.POST['content'],
        )
        return redirect('list')
    
    return render(request, 'new.html')

#Quaeryset 추가공부하기... (전달형태 위주로 / 저장되어 있는 데이터 모습 그려보기)
def list(request):
    articles = Article.objects.all()
    articles_category = Article.objects.values('category')
    NumHobby = len(Article.objects.filter(category ="hobby"))
    NumFood = len(Article.objects.filter(category ="food"))
    NumProgramming = len(Article.objects.filter(category ="programming"))


    return render(request, 'list.html', {'articles': articles, 'articles_category': articles_category, 
    'NumHobby': NumHobby, 'NumFood' : NumFood, 'NumProgramming':NumProgramming, })

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article': article})

def category(request, article_category):
    categorygroup = Article.objects.filter(category = article_category)
    return render(request, 'category.html', {'articles': categorygroup, 'category': article_category})