from django import template
from ..models import Article, Menu
from django.shortcuts import render
from django.core import serializers

from json import dumps
register = template.Library()


# функция чтобы найти под статьи
def child_find(articles, parent_id):
    childs = []
    for article in articles:
        if article['parent_id'] == parent_id:
            childs.append(article)
    return childs


# template tag для создания древовидного меню
@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):

    articles = Article.objects.filter(menu__menu_name=menu_name).values('id', 'parent_id', 'title', 'slug')
    menu = []
    # нахожу у каких статей есть подстатьи
    for article in articles:
        childs = child_find(articles, article['id'])
        if childs:
            article['childs'] = childs
        else:
            article['childs'] = False
    for article in articles:
        menu.append(article)

    # определяю какие статьи надо раскрыть
    if 'article' in context:
        articles_to_expand = []
        article_to_expand = context['article'].__dict__
        while True:
            if not article_to_expand['parent_id']:
                articles_to_expand.append(article_to_expand['id'])
                break
            else:
                articles_to_expand.append(article_to_expand['id'])
                for article in menu:
                    if article['id'] == article_to_expand['parent_id']:
                        article_to_expand = article
                        break
    else:
        articles_to_expand = False

    return {'menu': dumps(menu), 'articles_to_expand': articles_to_expand}
