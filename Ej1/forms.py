from django import forms
import re

dias_semana = [
    ('lunes', 'Lunes'),
    ('martes', 'Martes'),
    ('miércoles', 'Miércoles'),
    ('jueves', 'Jueves'),
    ('viernes', 'Viernes'),
    ('sábado', 'Sábado'),
    ('domingo', 'Domingo'),
]


class FormularioFechaEmail(forms.Form):
    fecha_inicio = forms.DateField(label='fecha de inicio', input_formats=['%d/%m/%Y'])
    fecha_fin = forms.DateField(label='fecha de fin', input_formats=['%d/%m/%Y'],
                                help_text='La fecha de fin tiene que ser igual o superior a la fecha de inicio ')
    dias_semana = forms.MultipleChoiceField(label='fecha de fin', choices=dias_semana,
                                            widget=forms.CheckboxSelectMultiple, help_text='Elige maximo 3')
    email = forms.EmailField(label='Email', help_text='El email tiene que pertenecer a IESMartinezm')

    def clean_fecha_fin(self):
        fecha_inicio = self.cleaned_data.get('fecha_inicio')
        fecha_fin = self.cleaned_data.get('fecha_fin')

        if fecha_fin < fecha_inicio:
            raise forms.ValidationError("La fecha de fin tiene que ser posterior a al fecha de inicio")
        return fecha_fin

    def clean_dias_semana(self):
        dias_semana = self.cleaned_data.get('dias_semana')

        if len(dias_semana) > 3:
            raise forms.ValidationError("El maximo de dias que se pueden seleccionar son 3")
        return dias_semana

    def clean_email(self):
        email = self.cleaned_data.get('email')
        pattern_email = r'.*@iesmartinezm\.es$'
        if not (re.match(pattern_email, email)):
            raise forms.ValidationError("El correo no pertenece a IES Martinez Montañes")
        return email
