from django import forms

from .models import Student


class StudentModelForm(forms.ModelForm):
    class Meta:
        model= Student

        fields='__all__'

        #fields=['name', 'age']
        labels={
        "name":"Enter First Name:"
        }
        #exclude=['name', 'age']


from django import forms
from .models import Employee


class EmpModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Employee Name"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Email address"
            }),
            "salary": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Salary"
            }),
            "depart": forms.Select(attrs={
                "class": "form-select"
            }),
        }
        