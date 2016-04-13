#coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from helloDjango.core.models import Speaker

class SpeakerDetailTest(TestCase):
    def setUp(self):
        Speaker.objects.create(name='Fulano de Tal',
                               slug='fulano-de-tal',
                               url='http://meusite.net',
                               description='Example for description!')
                               
        url = reverse('core:speaker_detail', kwargs={'slug': 'fulano-de-tal'})
        self.resp = self.client.get(url)

    def test_get(self):
        'GET should result in 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, "core/speaker_detail.html")

    def test_html(self):
        'Testing basics of HTML'
        self.assertContains(self.resp, 'Fulano de Tal')
        self.assertContains(self.resp, 'Example for description!')
        self.assertContains(self.resp, 'http://meusite.net')

    def test_context(self):
        'Speaker must be in context'
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)

class SpeakerNotFound(TestCase):
    def test_not_found(self):
        url = reverse('core:speaker_detail', kwargs={'slug': 'john-doe'})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)
