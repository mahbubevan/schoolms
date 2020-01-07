from django.shortcuts import render,redirect
from . models import Staff
# Create your views here.

def dashboard(request):
    try:
        get_logged_in_user_id = request.session['staff_id']
    except KeyError:
        return redirect('account:login')

    try:
        staff = Staff.objects.get(id=get_logged_in_user_id)
    except Staff.DoesNotExist:
        staff = None 

    if staff is not None:
        context = {
            'staff':staff,
        }
        return render(request,'staff/dashboard.html',context)
    return redirect('account:login')