from django.test import TestCase
from helloDjango.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r
class SucessTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(name='azk4n', cpf='66666666888', email='teste@mail.com', phone='23-99883888')
        self.resp = self.client.get(r('subscriptions:success', args=[s.pk]))

    def test_get(self):
        'GET /incricao/1/ deve retornar status_code 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        'Contexto tem que ter uma instancia de subscription'
        #import pdb
        #pdb.set_trace()
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        self.assertContains(self.resp, 'azk4n')

class SuccessNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get(r('subscriptions:success', args=[0]))
        self.assertEqual(404, response.status_code)
