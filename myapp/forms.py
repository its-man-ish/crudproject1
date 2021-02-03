from .models import StudentModel
from django import forms

class StudentForm(forms.ModelForm):
   
    class Meta:
        model = StudentModel
        fields = ['name','email','grade']
        labels = {
            'name':'Student Name',
            'email':'Student Email-Id',
            'grade':'Class',
        }

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'grade':forms.TextInput(attrs={'class':'form-control'}),
        }