from django.shortcuts import render, redirect
from .models import BMIRecord
from .forms import BMIForm

def calculate_bmi(request):
    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            bmi_record = form.save(commit=False)
            bmi_record.bmi = bmi_record.weight / (bmi_record.height * bmi_record.height)
            bmi_record.save()
            return redirect('bmi_results')

    else:
        form = BMIForm()

    return render(request, 'calculator/bmi_form.html', {'form': form})

def bmi_results(request):
    records = BMIRecord.objects.all()
    return render(request, 'calculator/bmi_results.html', {'records': records})
