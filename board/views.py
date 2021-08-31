from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import Board
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import BoardForm

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username, email, password)
            return redirect('list')
        except IntegrityError:
            context = {
              'error_message' : 'このユーザーはすでに存在しています。'
            }
            return render(request, 'user/signup.html', context)
            
    return render(request, 'user/signup.html', {})

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,  password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'user/login.html', { 'context' : 'ログインできませんでした。'})

    return render(request, 'user/login.html', {})

def signout(request):
    logout(request)
    return redirect('login')

@login_required
def list(request):
    board_list = Board.objects.all()
    return render(request, 'user/list.html', { 'board_list' : board_list })

@login_required
def detail(request, pk):
    board_object = get_object_or_404(Board, pk=pk) # 右側のpkが上の(request, pk)のpkに対応している
    return render(request, 'user/detail.html', { 'board_object' : board_object })

def good(request, pk):
    post = Board.objects.get(pk=pk)
    post.good += 1 
    post.save()
    return redirect('list')

def read(request, pk):
    post = Board.objects.get(pk=pk)
    username = request.user.get_username()
    if username in post.readtext:
        return redirect('list')
    else :
        post.read += 1
        post.readtext = post.readtext + ' ' + username
        post.save()
        return redirect('list')

class BoardCreate(CreateView):
    template_name = 'user/create.html'
    model = Board
    form_class = BoardForm
    success_url = reverse_lazy('list')