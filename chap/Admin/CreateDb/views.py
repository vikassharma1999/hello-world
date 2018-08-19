from django.shortcuts import render,redirect
from .forms import DocumentForm

# Create your views here.
def CreateDb(request):
	return render(request,'CreateDb/create.html')
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'CreateDb/model_form_upload.html', {
        'form': form
    })