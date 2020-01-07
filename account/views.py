from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, make_password
# Importing Models
from staff . models import Staff
from student .gen_std_id import get_std_id

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
        # hash_pass = make_password(password)
        is_start_with_number = username[0].isdigit()

        if is_start_with_number:
            if Staff.objects.filter(teacher_id=username).exists():
                s_user = Staff.objects.get(teacher_id=username)
                if check_password(password,s_user.password):
                    request.session['staff_id'] = s_user.id
                    return redirect('staff:dashboard')
                return redirect('account:login')
            return redirect('account:login')
        else:
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

@login_required(login_url='/account/login/')
def view_teacher(request):
    staffs = Staff.objects.all()
    context = {
        'staffs':staffs,
        'teacher_id':get_std_id(),
    }

    return render(request,'account/manage_teacher.html',context)


def create_teacher(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username    = request.POST['username']
        password    = make_password(request.POST['password'])
        role        = request.POST['role']
        teacher_id  = request.POST['teacher_id']

        staff = Staff.objects.create(first_name=first_name,last_name=last_name,username=username,password=password,role=role,teacher_id=teacher_id)
        staff.save()

        return redirect('account:view_teacher')
    
def logout_custom_user(request):
    try:
        del request.session['staff_id']
    except KeyError:
        pass

    return redirect('account:login')