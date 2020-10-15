from django import forms
from .models import Inscricao


class Cadastrocriar(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['nome', 'cpf', 'nascimento', 'email', 'telefone', 'CEP',
                  'escolaridade', 'profissao']
