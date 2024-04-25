from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from .models import Chat, Message
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .utils import check_username_exists, check_email_exists, check_password_match

@login_required(login_url='/login/')

def index(request):
    if request.method == 'POST':
        print("received data: " + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        new_message = Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)

        new_message_json_alt = {
            'textmessage': new_message.text,
            'author': new_message.author.username,
            'created_at': new_message.created_at,
        }
        return JsonResponse(new_message_json_alt, safe=False)
        
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': chatMessages})

def login_view(request):
    context = {}
    redirect = request.GET.get('next', '/chat/')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        has_error = check_username_exists(username, context)
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(request.POST.get('redirect'))
        else:
            if not has_error:
                context["userNotExists"] = True
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
        username = request.POST.get('username').lower()
        email = request.POST.get('email')
        password = request.POST.get('password')
        repeatPassword = request.POST.get('repeatPassword')
    
        has_error = check_username_exists(username, context)
        has_error |= check_email_exists(email, context)
        has_error |= check_password_match(password, repeatPassword, context)
        if not has_error:
            user = User.objects.create_user(username=username,
                                 password=password, email=email)
            if user:
                return redirect('/login/')
        return render(request, 'authenticate/register.html', context)  
    else:
        return render(request, 'authenticate/register.html')