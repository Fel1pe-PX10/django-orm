from django import forms

from applications.libro.models import Libro

from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    
    class Meta:
        model = Prestamo
        fields = (
            'lector',
            'libro'
        )


class PrestamoMultipleForm(forms.ModelForm):
    
    libros = forms.ModelMultipleChoiceField(
        queryset=None,
        required=True,
        widget=forms.CheckboxSelectMultiple
    )
    
    class Meta:
        model = Prestamo
        fields = (
            'lector',
        )
        
    def __init__(self, *args, **kwargs):
        super(PrestamoMultipleForm, self).__init__(*args, **kwargs)
        self.fields['libros'].queryset = Libro.objects.all()