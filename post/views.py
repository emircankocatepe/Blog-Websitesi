from django.shortcuts import render, HttpResponse

# Create your views here.

def post_index(request):
    return HttpResponse('Burasi post index sayfasi')

def post_detail(request):
    return HttpResponse('Burasi post detail sayfasi')

def post_create(request):
    return HttpResponse('Burasi post create sayfasi')

def post_update(request):
    return HttpResponse('Burasi post update sayfasi')

def post_delete(request):
    return HttpResponse('Burasi post delete sayfasi')