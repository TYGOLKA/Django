from django.shortcuts import render, redirect
from .forms import ApplicantForm

def home(request):
    return render(request, 'admissions/home.html')
def applicant_form(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ApplicantForm()
    return render(request, 'admissions/applicant_form.html', {'form': form})

def success(request):
    return render(request, 'admissions/success.html')
