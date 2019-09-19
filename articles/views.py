from django.shortcuts import render, redirect, get_object_or_404
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
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

#입력페이지 제공
#GET /articles/create/ -> 페이지만 받아가겠다.
# def new(request):
#     return render(request, 'articles/new.html')


#데이터를 전달받아 article 생성하는 페이지
#POST /articles/create/
def create(request):
    # 요청이 POST라면 사용자 데이터 받아서 article 생성
    # /articles/new/의 new.html의 form에서 전달받은 데이터들
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        article = Article()
        article.title = title
        article.content = content
        article.save()

        return redirect('articles:detail', article.pk)  

    else:
        # 만약 GET 요청으로 들어오면 html 페이지 렌더링
        return render(request, 'articles/create.html')


def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST': 
        article.delete()
        return redirect('articles:index')

    else:
        return redirect('articles:detail', article_pk)

def update(request, article_pk):
    # POST : 실제 UPDATE 로직 수행
    # GET : UPDATE를 하기위한 FORM을 제공하는 페이지
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article.title = title
        article.content = content
        article.save()
        
        return redirect('articles:detail', article.pk)  

    else:
        context ={
            'article' : article,
        }
        return render(request, 'articles/update.html', context)