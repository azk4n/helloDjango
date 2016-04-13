#codigo: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
#codigo refatorado
class HomePageTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('core:homepage'))

    def test_get(self):
        'Testa se o status code da requisicao eh 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'testa se o template utilizado eh o index.html'
        self.assertTemplateUsed(self.resp, "core/index.html")














#codigo nao-fatorado
#class HomepageTest(TestCase):
#    def test_get(self):
#        'GET / must return status code 200'
#        response = self.client.get('/')
#        self.assertEqual(200, response.status_code)
#        self.assertTemplateUsed(response, 'index.html')
