#coding: utf-8
from django.test import TestCase
from helloDjango.subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):
    def test_has_fields(self):
        'testa se form tem 4 campos'
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'cpf', 'email', 'phone'], form.fields)

    def make_validated_form(self, **kwargs):
        data = dict(name='ALEXANDRE', cpf='66666666888', email='teste@mail.com',
                    phone_0='22', phone_1='12345668')
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form

    def test_cpf_is_digit(self):
        'CPF deve receber apenas numeros'
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertItemsEqual(['cpf'], form.errors)

    def test_cpf_has_11_digits(self):
        'CPF deve ter 11 digitos'
        form = self.make_validated_form(cpf='1234')
        self.assertItemsEqual(['cpf'], form.errors)

    def test_name_must_be_capitalized(self):
        'Nome deve ser MAIUSCULO'
        form = self.make_validated_form(name=u'ALEXANDRE Guimaraes')
        self.assertEqual(u'Alexandre Guimaraes', form.cleaned_data['name'])

    def test_email_is_optional(self):
        'Email é opcional'
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        'Email e Telefone são opcionais, mas ao menos um deve ser informado'
        form = self.make_validated_form(email='', phone_0='', phone_1='')
        self.assertItemsEqual(['__all__'], form.errors)
