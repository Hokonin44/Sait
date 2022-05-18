from django.shortcuts import render
from django.http import HttpResponse, Http404
from post_app.models import News


def test(request):
    return HttpResponse('<h1 style="color:red;">Hello World!</h1>')


def test1(request):
    dict_ = {
        'title': 'Blog APPLICATION',
        'text': 'HELLO WORLD!',
        'date': ''
    }
    return render(request, 'hello.html', context=dict_)


def news_list_view(request):
    news_list = News.objects.all()
    context = {
        'news': news_list
    }
    return render(request, 'news.html', context=context)


def news_detail_view(request, id):
    try:
        news_detail = News.objects.get(id=id)
    except News.DoesNotExist:
        raise Http404('News not FOUND!!!')
    return render(request, 'news_detail.html', context={
        'detail': news_detail
    })