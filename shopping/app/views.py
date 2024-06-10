from django.shortcuts import render,redirect
from app.models import Guest
from django.contrib import messages


# Create your views here.

def home(request):
    user = Guest.objects.all()
    return render(request,'home.html',{'users':user})

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = Guest.objects.create(username=username,password=password)
        user.save()
        messages.success(request,"Signin SuCCESS")
        return redirect('login')
    
    return(render(request,'signup.html'))

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = Guest.objects.filter(username=username,password=password).exists()
        if user:
            messages.success(request,"Login SuCCESS")
            return redirect('home')
        
        else:
            return redirect('signup')
        
    return render(request,'login.html')
        
    
def  delet(request):
    users = Guest.objects.all()
    for user in users:
        user.delete()
    
    return redirect('home')