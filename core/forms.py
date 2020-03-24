from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML
# from django.forms.widgets import Select
from .interface import e_bisexto


class TransFormEdit(forms.Form):
    trans_dia = forms.IntegerField(
        label="Dia: ",
        required=True
    )
    trans_mes = forms.IntegerField(
        label="Mes: ",
        required=True
    )
    trans_ano = forms.IntegerField(
        label="Ano: ",
        required=True
    )
    trans_valor = forms.FloatField(
        label="Valor: ",
        required=True
    )
    trans_conta = forms.CharField(
        label="Conta: ",
        max_length=20,
        required=True
    )
    trans_meio = forms.CharField(
        label="Meio Pagto: ",
        max_length=2,
        required=True
    )
    trans_descr = forms.CharField(
        label="Descrição: ",
        max_length=80,
        required=False
    )
    trans_emprest = forms.CharField(
        label="Nome Empréstimo *: ",
        max_length=30,
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(TransFormEdit, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('trans_dia', css_class='form-group col-md-2 mb-0'),
                Column('trans_mes', css_class='form-group col-md-2 mb-0'),
                Column('trans_ano', css_class='form-group col-md-2 mb-0')
            ),
            Row(
                Column('trans_valor', css_class='form-group col-md-4 mb-0'),
                Column('trans_conta', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('trans_meio', css_class='form-group col-md-5 mb-0')
            ),
            Row(
                Column('trans_descr', css_class='form-group col-md-4 mb-0'),
                Column('trans_emprest', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Salvar'),
            HTML('<a class="btn btn-danger" href="/trans/">Voltar</a>')
        )

    def clean(self):
        cleaned_data = super().clean()
        dia = cleaned_data.get('trans_dia')
        mes = cleaned_data.get('trans_mes')
        ano = cleaned_data.get('trans_ano')
        print(dia, mes, ano)
        if mes in (1, 3, 5, 7, 8, 10, 12):
            qtdedias = 31
        elif mes == 2:
            if e_bisexto(ano):
                qtdedias = 29
            else:
                qtdedias = 28
        else:
            qtdedias = 30
        if 0 < dia <= qtdedias:
            pass
        else:
            raise forms.ValidationError('Dia inválido !')

    # def clean_trans_dia(self):
    #    dia = self.cleaned_data.get('trans_dia')
    #    if dia > 31 or dia < 1:
    #        raise forms.ValidationError('Dia inválido!')
    #    return dia
