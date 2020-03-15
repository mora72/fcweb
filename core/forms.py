from django import forms
from .models import Grupo, Integrante
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML
from django.forms.widgets import Select


class GrupoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GrupoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.layout = Layout(
            Row(
                Column('cidade', css_class='form-group col-md-4 mb-0'),
                Column('uf', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('dataini', css_class='form-group col-md-5 mb-0')
            ),
            Row(
                Column('nomecontato', css_class='form-group col-md-4 mb-0'),
                Column('telefonecontato', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('status', css_class='form-group col-md-4 mb-0')
            )
        )

        for f in self.fields:
            #  self.fields[f].label = _(self.fields[f].label)
            if isinstance(self.fields[f].widget, Select):
                self.fields[f].widget.attrs['disabled'] = 'disabled'
            else:
                self.fields[f].widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Grupo
        fields = ('status', 'cidade', 'uf', 'dataini', 'nomecontato', 'telefonecontato')
        labels = {
            'status': 'Situação do Grupo: ',
            'dataini': 'Data de Início (AAAA/MM/DD):',
            'nomecontato': 'Nome para Contato: ',
            'telefonecontato': 'Telefone de Contato: ',
            'uf': 'Estado: ',
            'cidade': 'Cidade: '
        }


class GrupoFormEdit(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GrupoFormEdit, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('nome', css_class='form-group col-md-4 mb-0')
            ),
            Row(
                Column('cidade', css_class='form-group col-md-4 mb-0'),
                Column('uf', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('dataini', css_class='form-group col-md-5 mb-0')
            ),
            Row(
                Column('nomecontato', css_class='form-group col-md-4 mb-0'),
                Column('telefonecontato', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('status', css_class='form-group col-md-4 mb-0')
            ),
            Submit('submit', 'Salvar'),
            HTML('<a class="btn btn-danger" href="/">Voltar</a>')
        )

    class Meta:
        model = Grupo
        fields = ('nome', 'status', 'cidade', 'uf', 'dataini', 'nomecontato', 'telefonecontato')
        labels = {
            'nome': 'Nome do Grupo: ',
            'status': 'Situação do Grupo: ',
            'dataini': 'Data de Início (MM/DD/AAAA):',
            'nomecontato': 'Nome do Contato: ',
            'telefonecontato': 'Telefone de Contato: ',
            'uf': 'Estado: ',
            'cidade': 'Cidade: '
        }


class IntegranteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IntegranteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.layout = Layout(
            Row(
                Column('grupo', css_class='form-group col-md-3 mb-0'),
                Column('cidade', css_class='form-group col-md-3 mb-0'),
                Column('uf', css_class='form-group col-md-2 mb-0')
            ),
            Row(
                Column('telefone', css_class='form-group col-md-2 mb-0'),
                Column('email', css_class='form-group col-md-4 mb-0'),
                Column('status', css_class='form-group col-md-3 mb-0')
            ),
            Row(
                Column('genero', css_class='form-group col-md-2 mb-0'),
                Column('estadocivil', css_class='form-group col-md-2 mb-0'),
                Column('datanasc', css_class='form-group col-md-4 mb-0')
            ),
        )

        for f in self.fields:
            #  self.fields[f].label = _(self.fields[f].label)
            if isinstance(self.fields[f].widget, Select):
                self.fields[f].widget.attrs['disabled'] = 'disabled'
            else:
                self.fields[f].widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Integrante
        fields = ('grupo', 'cidade', 'uf', 'genero', 'datanasc', 'estadocivil',
                  'telefone', 'email', 'status')
        labels = {
            'grupo': 'Grupo: ',
            'cidade': 'Cidade: ',
            'uf': 'UF: ',
            'genero': 'Gênero: ',
            'datanasc': 'Data Nascimento AAAA/MM/DD:',
            'estadocivik': 'Estado Civil: ',
            'telefone': 'Telefone: ',
            'email': 'Email: ',
            'status': 'Situação: '
        }


class IntegranteFormEdit(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IntegranteFormEdit, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('nome', css_class='form-group col-md-4 mb-0')
            ),
            #  Row(Column('foto', css_class='form-group col-md-6 mb-0')),
            Row(
                Column('grupo', css_class='form-group col-md-3 mb-0'),
                Column('cidade', css_class='form-group col-md-3 mb-0'),
                Column('uf', css_class='form-group col-md-3 mb-0')
            ),
            Row(
                Column('telefone', css_class='form-group col-md-2 mb-0'),
                Column('email', css_class='form-group col-md-4 mb-0'),
                Column('status', css_class='form-group col-md-3 mb-0')
            ),
            Row(
                Column('genero', css_class='form-group col-md-2 mb-0'),
                Column('estadocivil', css_class='form-group col-md-2 mb-0'),
                Column('datanasc', css_class='form-group col-md-4 mb-0')
            ),
            Row(
                Column('foto', css_class='form-group col-md-5 mb-0')
            ),
            Submit('submit', 'Salvar'),
            HTML('<a class="btn btn-danger" href="/integrantes/">Voltar</a>')
        )

    class Meta:
        model = Integrante
        fields = ('nome', 'grupo', 'cidade', 'uf', 'genero', 'datanasc', 'estadocivil',
                  'telefone', 'email', 'status', 'foto')
        labels = {
            'nome': 'Nome do Integrante: ',
            'grupo': 'Grupo: ',
            'cidade': 'Cidade: ',
            'uf': 'UF: ',
            'genero': 'Gênero: ',
            'datanasc': 'Data Nascimento MM/DD/AAAA:',
            'estadocivik': 'Estado Civil: ',
            'telefone': 'Telefone: ',
            'email': 'Email: ',
            'status': 'Situação: ',
            'foto': 'Foto: '
        }
