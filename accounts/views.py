from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm, ContactForm

# Create your views here.

from django.contrib.auth import authenticate, login, logout

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'accounts/form.html', {'form' : form, 'title': 'Giris Yap'})

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.is_staff = user.is_superuser = True
        
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('home')
    return render(request, 'accounts/form.html', {'form' : form, 'title': 'Uye Ol'})


def logout_view(request):
    logout(request)
    return redirect('home')

def about_view(request):
    return render(request, 'about/about.html')

def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return render(request, 'about/success.html')
    return render(request, 'about/contact.html', {'form': form, 'title' : 'Write to us'})

