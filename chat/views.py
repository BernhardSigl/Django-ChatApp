from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from .models import Chat, Message
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.core import serializers

@login_required(login_url='/login/')

def index(request):
    if request.method == 'POST':
        print("received data: " + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        new_message = Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
        
        # new_message_json = serializers.serialize('json', [ new_message, ]) # ungenaues json
        
        new_message_json_alt = {
            'textmessage': new_message.text,
            'author': new_message.author.username,
            'created_at': new_message.created_at,
        }
        
        return JsonResponse(new_message_json_alt, safe=False) # mit [1:-1] array to json
        
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': chatMessages})

def login_view(request):
    context = {}
    redirect = request.GET.get('next', '/chat/')
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect(request.POST.get('redirect'))
        else:
            context["wrongPassword"] = True
            context['username'] = request.POST.get('username')
            context["redirect"] = redirect
            return render(request , 'authenticate/login.html', context)
    else:
        return render(request, 'authenticate/login.html', {'redirect': redirect})

def register_view(request):
    context = {}
    if request.method == 'POST':
        if request.POST.get('password') == request.POST.get('repeatPassword'):
            user = User.objects.create_user(username=request.POST.get('username'),
                                 password=request.POST.get('password'), email=request.POST.get('email'))
            if user:
                return redirect('/login/')
        else:
            context["wrongRepeatPassword"] = True
            context['username'] = request.POST.get('username')
            context['email'] = request.POST.get('email')
            print('4')
            return render(request, 'authenticate/register.html', context)
    else:
        return render(request, 'authenticate/register.html')