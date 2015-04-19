from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader


def compare(request):
    template = loader.get_template('faces/compare.html')
    context = RequestContext(request, {
        'url1': "http://risovach.ru/upload/2013/06/mem/ya-tvoi-dom-truba-shatal_21385844_orig_.jpg",
        'url2': "http://troll-face.ru/static/mememaker/f/c/24817-vasya-afrika.jpg",
    })
    return HttpResponse(template.render(context))
