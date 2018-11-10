from django import forms

from afluente.demo.models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = 'nome status servico imagem'.split()
