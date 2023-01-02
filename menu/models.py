from django.db import models


class Menu(models.Model):
    menu_name = models.CharField(max_length=100, db_index=True, unique=True, verbose_name="Название меню")

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.menu_name


class Article(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name="Название")
    text = models.TextField(blank=True, verbose_name="Текст")
    slug = models.SlugField(max_length=250, db_index=True, unique=True)
    menu = models.ForeignKey('Menu', null=True, related_name='article', on_delete=models.SET_NULL, verbose_name="Меню")
    parent = models.ForeignKey('Article', blank=True, null=True, related_name='child', on_delete=models.SET_NULL, verbose_name="Родительская статья")

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
