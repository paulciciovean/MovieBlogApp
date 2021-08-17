from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegister

def register(request):
    if request.method=="POST":
        form = UserRegister(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'The acount was created successfully ')
            return redirect('users-login')

    else:
        form = UserRegister()
    return render(request,'users/register.html',{ 'form':form })
