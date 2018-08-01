from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.
def login_page(request):
	if request.method=='POST':
		form=AuthenticationForm(data=request.POST)
		if form.is_valid():
			user=form.get_user()
			login(request,user)
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:
				return redirect('home')
	else:
		form=AuthenticationForm()
	return render(request,'Auth/login_page.html',{'form':form})
def signup_page(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			user=form.save()
			login(request,user)
			return redirect('home')
	else:
		form=UserCreationForm()
	return render(request,'Auth/signup_page.html',{'form':form})
def logout_page(request):
	if request.method=='POST':
		logout(request)
		return redirect('home')