from django import forms
import re
from django.utils import timezone


def comprobar_requisitos(texto):
    tiene_caracter_especial = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', texto))
    tiene_numero = bool(re.search(r'[1-9]', texto))
    tiene_minuscula = bool(re.search(r'[a-z]', texto))
    tiene_mayuscula = bool(re.search(r'[A-Z]', texto))

    return (
        tiene_caracter_especial and
        tiene_numero and
        tiene_minuscula and
        tiene_mayuscula
    )


class FormularioNombreCont(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password', widget=forms.PasswordInput, min_length=8)
    fecha_acceso = forms.DateTimeField(initial=timezone.now())

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username.lower() in password.lower():
            raise forms.ValidationError("La contraseña no puede contener al usuario")

        if not (comprobar_requisitos(password)):
            raise forms.ValidationError("""La contraseña tiene que contener una minuscula,
                                         una mayuscula, un numero y un caracter especial""")

        return password

    def clean_fecha_acceso(self):
        fecha_acceso = self.cleaned_data.get('fecha_acceso')
        time_diference = timezone.now() - fecha_acceso
        if time_diference.min > 60:
            raise forms.ValidationError('Han pasado mas de dos minutos')

        return fecha_acceso
