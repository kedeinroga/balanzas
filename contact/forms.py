from django import forms
from phonenumber_field.formfields import PhoneNumberField

class ContactForm(forms.Form):
    empresa = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe el nombre de la empresa'}
    ), min_length=3, max_length=100)
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
    ), min_length=3, max_length=100)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu email'}
    ), min_length=3, max_length=100)
    service = forms.CharField(label="Servicio", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe el servicio'}
    ), min_length=3, max_length=50)
    phone = forms.CharField(label="Teléfono", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu teléfono:'}
    ), min_length=7, max_length=12)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-input textarea-lg', 'rows': 3, 'placeholder':'Escribe tu mensaje'}
    ), min_length=10, max_length=1000)
    