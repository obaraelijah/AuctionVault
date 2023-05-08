from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from ..aunctionItem.models import Contact, WishList

def register(request):
    if request.method =='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirmPassword=request.POST['confirmPassword']
        
        if password == confirmPassword:
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.ERROR, 'Username taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.add_message(request, messages.ERROR, 'Email Already Exist!')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
                    user.save()
                    messages.add_message(request, messages.SUCCESS, 'You are now registered,please log in')
                    return redirect('login')
                
        else:
            messages.add_message(request, messages.ERROR, 'Passwords does not match')
            return redirect('register')
            
    return render(request,'register.html')