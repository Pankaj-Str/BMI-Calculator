from django.shortcuts import render
from django.http import JsonResponse

def calculate_bmi(request):
    if request.method == 'POST':
        weight = float(request.POST['weight'])
        height = float(request.POST['height'])
        bmi = weight / (height ** 2)
        return JsonResponse({'bmi': bmi})
    else:
        return render(request, 'calculator/bmi_form.html')
