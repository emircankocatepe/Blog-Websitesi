from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Post
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator
from .forms import PostForm, CommentForm
from django.db.models import Q

# Create your views here.

def post_index(request):
    post_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(
            Q(baslik__icontains=query) |
            Q(metin__icontains=query) | 
            Q(user__first_name__icontains = query) |
            Q(user__last_name__icontains = query)
            ).distinct()
    
    paginator = Paginator(post_list, 4)  # Show 25 contacts per page.

    page = request.GET.get("page")
    posts = paginator.get_page(page)

    return render(request, 'post/index.html', {'posts' : posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())


    context = {
        'post' : post,
        'form' : form,
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
        post = form.save(commit=False)
        post.user = request.user
        post.save()
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