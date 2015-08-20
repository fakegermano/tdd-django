from django.contrib.auth import authenticate, login
from django.shortcuts import render

# Create your views here.


def login_page(request):
    if request.method == 'POST':
        context = {}
        if request.POST['username'] == '' and request.POST['password'] == '':
            context = {'error_messages': 'Username and Password missing!'}
        elif request.POST['username'] == '':
            context = {'error_messages': 'Username missing!'}
        elif request.POST['password'] == '':
            context = {'error_messages': 'Password missing!'}
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    context = {'login_status': 'Login Successfull!'}
            else:
                context = {'login_status': 'Login Failed!'}
        return render(request, 'login.html', context)
    return render(request, 'login.html')