from django import forms
from StoreApp.models import Cliente

class ContatoFrom(forms.Form):
    nome = forms.CharField()
    email = forms.CharField()
    telefone = forms.CharField()
    assunto = forms.CharField()
    mensagem = forms.CharField(widget=forms.Textarea)

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__alt__'