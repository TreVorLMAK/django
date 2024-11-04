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
from django.contrib import messages

def renderRegisterForm(request):
    if request.method == 'POST':
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
