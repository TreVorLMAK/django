<<<<<<< HEAD

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
=======
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User

# def renderRegisterForm(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         username = request.POST['username']
#         user = User.objects.create(
#          username = username,
#          email = email,
#          password = password,
#         )
#         user.set_password(password)
#         user.save()
#         return redirect('/blog/login')
    
#     else:
#         return render(request, 'auth/register.html')

# def renderLoginForm(request):
#     return render(request, 'auth/login.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
>>>>>>> c464e3426f14e6979fe4607f8c4da5e52888b5d5
from django.contrib import messages

def renderRegisterForm(request):
    if request.method == 'POST':
<<<<<<< HEAD
      username = request.POST['username']
      password = request.POST['password']
      email = request.POST['email']
      print(username,password,email)
      user = User.objects.create(
        username = username, 
        email = email, 
      )
      user.set_password(password)
      user.save()
      print(user, "User")
      return redirect('/blog/login')

    else:
        return render(request,'auth/register.html')


def renderLoginForm(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        print(username,password,user)
        if user is not None: 
            login(request,user)
            return redirect('/blog')
        else: 
            messages.error(request,"Invalid username or password")
            return redirect('/blog/login')
    return render(request,'auth/login.html')
=======
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        
        # Create the user instance without saving
        user = User(username=username, email=email)
        user.set_password(password)  # Securely hash the password
        user.save()  # Save the user to the database
        
        return redirect('/blog/login')
    
    else:
        return render(request, 'auth/register.html')

def renderLoginForm(request):
    if request.method == 'post':
        email = request.post['email']
        password = request.post['password']
        user = authenticate(request, email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request, "Invalid email or password")
            return redirect('/blog/login')
    return render(request, 'auth/login.html')
>>>>>>> c464e3426f14e6979fe4607f8c4da5e52888b5d5
