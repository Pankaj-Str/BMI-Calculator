from django import forms
from .models import BMIRecord

class BMIForm(forms.ModelForm):
    class Meta:
        model = BMIRecord
        fields = ['height', 'weight']
