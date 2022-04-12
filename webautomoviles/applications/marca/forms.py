from datetime import datetime
from django import forms
import datetime

class NewCocheForm(forms.Form):
    matr = forms.CharField(max_length=50)
    fecha = forms.DateField(initial=datetime.date.today)
    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)