from django.shortcuts import render

# Create your views here.


def login_page(request):
    if request.method == 'POST':
        if request.POST['username'] == '' and request.POST['password'] == '':
            context = {'error_messages': 'Username and Password missing!'}
        elif request.POST['username'] == '':
            context = {'error_messages': 'Username missing!'}
        elif request.POST['password'] == '':
            context = {'error_messages': 'Password missing!'}
        else:
            context = {'login_status': 'Login Successfull!'}
        return render(request, 'login.html', context)
    return render(request, 'login.html')