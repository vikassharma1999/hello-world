from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .import forms
from .models import Uploaddb 
# Create your views here.
def Login(request):
	if request.method=='POST':
		form=AuthenticationForm(data=request.POST)
		if form.is_valid():
			user=form.get_user()
			login(request,user)
			if('next' in request.POST):
				return redirect(request.POST.get('next'))
			else:
				return redirect('home')
	else:
	    form=AuthenticationForm()
	return render(request,'Auth/login.html',{'form':form})
def Signup(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			user=form.save()
			login(request,user)
			return redirect('home')
	else:
		form=UserCreationForm()
	return render(request,'Auth/signup.html',{'form':form})
def AddFile(request):
	if request.method=="POST":
		form=forms.AddDb(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form=forms.AddDb()
	return render(request,'Auth/db.html',{'form':form})

def Logout(request):
	if request.method=="POST":
		logout(request)
		return redirect('home')