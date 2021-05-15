from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from .models import News


def index(request):
  news = News.objects.order_by('-created_at')

  paginator = Paginator(news, 6)
  page = request.GET.get('page')
  paged_news = paginator.get_page(page)

  context = {
    'news': paged_news,
  }

  return render(request, 'news/blog.html', context)


def news(request, news_id):
  news = get_object_or_404(News, pk=news_id)

  context = {
    'news': news,
  }

  return render(request, 'news/news.html', context)
