from .models import Log_table
from django.forms import ModelForm, TextInput, NumberInput


class Log_tableForm(ModelForm):
    class Meta:
        model = Log_table
        fields = {'log_time', 'text', 'height', 'width', 'scale', 'thickness'}

        widgets = {
            'text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            }),
            'height': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Высота экрана'
            }),
            'width': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ширина экрана'
            }),
            'scale': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Размер шрифта'
            }),
            'thickness': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Толщина шрифта'
            })
        }
