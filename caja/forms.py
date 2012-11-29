from django.forms import ModelForm
from caja.models import Fichero

class FicheroForm(ModelForm):
    class Meta:
        model = Fichero
        exclude = ('nombre',)