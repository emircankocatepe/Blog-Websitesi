from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .models import Post

from .forms import PostForm
# Create your views here.

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts' : posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    context = {
        'post' : post
    }

    return render(request, 'post/detail.html', context)

def post_create(request):
                
    ## form = PostForm(request)
    ##context = {
    ##    'form' : form,
    ## }

    ##if request.method == 'POST':
    ##    baslik = request.POST.get('baslik')
    ##    metin = request.POST.get('metin')
    ##    Post.objects.create(baslik = baslik, metin = metin)

    
    # if request.method == 'POST':
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         form.save()

    # else: 
    #     form = PostForm()

    form = PostForm(request.POST or None)

    if form.is_valid():
        post = form.save()
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form' : form,
    }
    
    return render(request, 'post/form.html', context)

def post_update(request, id):

    post = get_object_or_404(Post, id=id) # neden post'u asagida yukarida create metodunda yaptigimiz gibi form.save'a atamadik? guncellenmis yeni bir objects olmadi mi sonucta?

    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
            'form' : form,
        }
    
    return render(request, 'post/form.html', context)

def post_delete(request , id):

    post = get_object_or_404(Post, id=id)
    post.delete()

    return redirect('post:home')