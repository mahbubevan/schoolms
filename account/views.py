from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                # usrename already taken
                return redirect('account:registration')
            else:
                if User.objects.filter(email=email).exists():
                    # email already taken
                    return redirect('account:registration')
                else:
                    user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    # created new acc
                    return redirect('account:login')
        else:
            # password didnt match
            return redirect('account:registration')


    return render(request,'account/registration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('account:dashboard')
        return redirect('account:login')

    return render(request,'account/login.html')


def logout(request):
    auth.logout(request)
    return redirect('account:login')


@login_required(login_url='/account/login/')
def dashboard(request):
    return render(request,'account/dashboard.html')