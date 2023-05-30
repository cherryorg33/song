from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def register(request): 
       if request.method == 'POST': 
        first_name = request.POST['first_name']
        last_name = request.POST['last_name'] 
        username = request.POST['username']
        email =request.POST['email'] 
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
               if User.objects.filter(username=username).exists(): 
                messages.info(request, 'Email is exist ')
                return redirect(register)
        else: 
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()
                return redirect('login_user')

       else:
         print("this is not post method")
         return render(request,"register.html")
       
def login_user(request):
    if request.method == 'POST': 
           email =request.POST['email']
           password = request.POST['password'] 

           user = auth.authenticate(username=username, password=password) 
        if user is not None: 
            auth.login(request, user)
            return redirect('home')
            
        else: 
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user') 
  
    else: 
        return render(request, 'login.html')

def reo(request):
     if request.method=='POST':
          music_name=music_name(request.POST,request.file or None)
          public=request("public")
          private=request("private")
          protected=request("protected")
          if form.is_valid():
               form.savr()
               return redirect('reo.html')
          else:
               form=music_name()
               return render(request,'homee.html',{'form'form})
          
def logout_user(request):
         auth.logout(request)
         return redirect('home')

        


     
 

        