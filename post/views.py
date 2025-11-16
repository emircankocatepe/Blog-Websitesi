from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Post
from django.contrib import messages
from django.utils.text import slugify


from .forms import PostForm
# Create your views here.

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts' : posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post' : post
    }

    return render(request, 'post/detail.html', context)

def post_create(request):


    if not request.user.is_authenticated:
        return Http404()
                
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

    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        post = form.save()
        #post.slug = slugify(post.baslik.replace('ı','i'))
        #post.save()
        messages.success(request, "It's posted successfully!", extra_tags='message-success')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form' : form,
    }
    
    return render(request, 'post/form.html', context)

def post_update(request, slug):

    if not request.user.is_authenticated:
        return Http404()

    post = get_object_or_404(Post, slug=slug) # neden post'u asagida yukarida create metodunda yaptigimiz gibi form.save'a atamadik? guncellenmis yeni bir objects olmadi mi sonucta?

    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    if form.is_valid():
        form.save()
        messages.success(request, "It's updated successfully!", extra_tags='message-success')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
            'form' : form,
        }
    
    return render(request, 'post/form.html', context)

def post_delete(request , slug):

    if not request.user.is_authenticated:
        return Http404()

    post = get_object_or_404(Post, slug=slug)
    post.delete()

    return redirect('post:index')