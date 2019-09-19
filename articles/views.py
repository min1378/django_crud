from django.shortcuts import render, redirect
from .models import Article
# Create your views here.
#articles의 메인페이지, article list를 보여줌


def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

# variable Routing으로 사용자가 원하는 페이지를 pk로 받아 
# Detail 페이지를 보여준다.
def detail(request, article_pk):
    # SELECT * FROM articles WHERE pk=3 이런느낌의...
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

#입력페이지 제공
def new(request):
    return render(request, 'articles/new.html')


#데이터를 전달받아 article 생성하는 페이지
def create(request):
    # /articles/new/의 new.html의 form에서 전달받은 데이터들
    title = request.GET.get('title')
    content = request.GET.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article.pk)


def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()

    return redirect('articles:index')

