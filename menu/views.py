from django.shortcuts import render
from .models import Article, Menu


def index(request):
    return render(request, 'index.html')


def article(request, slug):
    article_object = Article.objects.get(slug=slug)
    return render(request, 'article.html', {'article': article_object})

