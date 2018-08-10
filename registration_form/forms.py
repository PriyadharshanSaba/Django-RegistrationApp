from django.forms import ModelForm
from registration_form.models import Register
from django import forms

class Reg_page1(ModelForm):
        class Meta:
            model = Register
            fields = ['phno','fullname', 'gender' , 'emailid','location' , 'teesize' , 'expr', 'dob']
            widgets = {
                'phno': forms.TextInput(attrs={'class': 'form-control' , 'placeholder' : 'Phone number'}),
                'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'User Name'}),
                'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Gender'}),
                'emailid': forms.TextInput(attrs={'class': 'form-control' , 'placeholder' : 'Email-ID'}),
                'location': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Location'}),
                'teesize': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'T-Shirt Size'}),
                'expr': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Number of Previous runs'}),
                'dob': forms.DateInput(attrs={'class': 'form-control','placeholder' : 'Date of Birth (DD/MM/YYYY)','id': 'datetimepicker12'}),
        }

class Bib_form(ModelForm):
        class Meta:
            model = Register
            fields = ['fullname' , 'emailid' , 'phno', 'bibno']
            widgets = {
                'phno': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Phone number'}),
                'fullname': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'User Name'}),
                'emailid': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Email-ID'}),
                'bibno': forms.NumberInput(attrs={'class': 'form-control','placeholder' : 'Bib Number'}),
        }
