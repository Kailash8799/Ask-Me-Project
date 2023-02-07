from django.shortcuts import render,redirect
from .models import Users
from user_auth.forms import UsersForm
# Create your views here.

def login(request):
    if(request.method == 'POST'):
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        return redirect('/')
        if len(email) > 5 and len(password) > 4:
            user_exits = Users.objects.filter(user_email=email)
            if(user_exits.user_password == password):
                pass
            else:
                pass
        else:
            pass
    else:
        pass
    return render(request,'user_auth/login.html')

# def signup(request):
#     if(request.method == 'POST'):
#         name = request.POST.get('name','')
#         email = request.POST.get('email','')
#         password = request.POST.get('password','')
#         if len(name) > 2 and len(email) > 5 and len(password) > 4:
#             user_exits = Users.objects.filter(user_email=email)
#             if(len(user_exits) == 0):
#                 user = Users(user_name=name,user_email=email,user_password=password)
#                 user.save()
#             else:
#                 pass
#         else:
#             pass
#     else:
#         pass
#     return render(request,'user_auth/signup.html')

def signup(request):
    if(request.method == 'POST'):
        form = UsersForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request,'user_auth/signup.html',{'form':form})
    else:
        form = UsersForm()
    return render(request,'user_auth/signup.html',{'form':form})

def forgot(request):
    return render(request,'user_auth/forgot.html')