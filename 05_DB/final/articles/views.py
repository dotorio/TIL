from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm(instance=article)
    context = {
        'form' : form,
        'article' : article
    }
    return render(request, 'articles/update.html', context)