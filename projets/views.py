from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Projet, Message, Skill
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from .forms import MessageForm


# Create your views here.
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except : 
            messages.error(request,'Username doest not exist')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'index')
        else:
            messages.error(request,'Password is incorrect')

    return render(request, 'projets/login.html')

def getIndex(request):
    projets = Projet.objects.all()
    skills = Skill.objects.all()
    context = {
        'projets' : projets,
        'skills': skills,
    }
    return render(request, 'projets/index.html', context)



def createMessage(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'projets/contact.html', context)


@login_required
def getMessages(request):
    tout_messages = Message.objects.all()
    context = {
        'tout_messages' : tout_messages
    }
    return render(request, 'projets/message.html', context)