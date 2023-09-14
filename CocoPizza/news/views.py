from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Article

class ArticlesListView(ListView):
    model = Article
    template_name = "news/news.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "news/article.html"
