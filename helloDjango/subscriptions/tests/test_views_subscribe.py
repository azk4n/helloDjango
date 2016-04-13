#coding: utf-8
from django.test import TestCase
from helloDjango.subscriptions.forms import SubscriptionForm
from helloDjango.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r


class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('subscriptions:subscribe'))
    def test_get(self):
        'testa se o status code recebido eh =200'
        self.assertEqual(200, self.resp.status_code)
    def test_template(self):
        'testa se o template usando eh o subscription_form'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')
    def test_html(self):
        'testa elementos do html'
        self.assertContains(self.resp, '<form')
        #self.assertContains(self.resp, '<input', 6)
        #self.assertContains(self.resp, 'type="text"', 4)
        self.assertContains(self.resp, 'type="submit"')
    def test_has_form(self):
        'testa se existe um formulário Django configurado'
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

class SubscribePostTest(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('subscriptions:subscribe'), {'name': 'azk4n', 'cpf':'12345678910', 'email':'azk5n@null.net', 'phone': '23-23213111'})

    def test_post(self):
        'POST valido redireciona p pagina de sucesso'
        self.assertEqual(302, self.resp.status_code)

    def test_save(self):
        self.assertTrue(Subscription.objects.exists())

class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('subscriptions:subscribe'), {'name': 'azk4n', 'cpf':'1234567893012', 'email':'azk5n@null.net', 'phone': '23-23213111'})
    def test_post(self):
        'post invalido nao redireciona'
        self.assertEqual(200, self.resp.status_code)
    def test_form_errors(self):
        self.assertTrue(self.resp.context['form'].errors)
    def test_dont_save(self):
        self.assertFalse(Subscription.objects.exists())

class TemplateRegressionTest(TestCase):
    def test_template_has_non_field_errors(self):
        'Verificar se erros de campos são exibidos no template'
        invalid_data = dict(
            name='azk4n',
            cpf='001234567890'
        )
        response = self.client.post(
            r('subscriptions:subscribe'),
            invalid_data)
        self.assertContains(response, '<ul class="errorlist">')
