#coding: utf-8

from django.test import TestCase
from helloDjango.subscriptions.admin import SubscriptionAdmin, Subscription, admin
from mock import Mock

class MarkAsPaidTest(TestCase):
    def setUp(self):
        self.model_admin = SubscriptionAdmin(Subscription, admin.site) #instancia model admin
        Subscription.objects.create(name='azk4n', cpf='66666666888', email='teste@mail.com')
    def test_has_action(self):
        'Action is installed'
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        queryset = Subscription.objects.all()
        mock = Mock()
        SubscriptionAdmin.message_user = mock
        self.model_admin.mark_as_paid(None, queryset)
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())
