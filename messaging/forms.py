from django import forms
from .models import Mensaje
from django.contrib.auth.models import User

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['destinatario', 'asunto', 'cuerpo']
        
    def __init__(self, *args, **kwargs):

        usuario_actual = kwargs.pop('usuario_actual', None)
        super(MensajeForm, self).__init__(*args, **kwargs)
        if usuario_actual:
            self.fields['destinatario'].queryset = User.objects.exclude(id=usuario_actual.id)