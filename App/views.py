from django.shortcuts import redirect, render
from .models import Drive
from .decorators import authenticated_user_only,unauthenticated_user_only
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

# Create your views here.
@unauthenticated_user_only
def login_user(request):
    context = {'template':'login'}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'invalid credentials')
    return render(request,'login_register.html',context)

@unauthenticated_user_only
def register(request):
    context = {'template':'register'}
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 != password2:
            messages.error(request,"Passwords donot match")
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists please login")
            return redirect('register')
        user = User.objects.create(username=username,email=email)
        user.set_password(password1)
        user.save()
        login(request,user)
        messages.success(request,'User Created Successfully')
        return redirect('index')
        
    return render(request,'login_register.html',context)

@authenticated_user_only
def index(request):
    context = {}
    if request.method == 'POST' and request.FILES:
        # Drive.objects.create(file=request.FILES['file'],name=request.POST['name'],size=request.POST['size'],extension=request.POST['extension'])
        # data = Drive.objects.all().order_by('-uploaded')
        context = {'files':''}
    return render(request,'index.html',context)    

def logout_user(request):
    logout(request)
    messages.success(request,'User Logout Successfull')
    return redirect('login')