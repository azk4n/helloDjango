from django.test import TestCase
from helloDjango.subscriptions.models import Subscription
from datetime import datetime
from django.db import IntegrityError

class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='azk4n',
            cpf='66666666888',
            email='teste@mail.com',
            phone='23-99883888'
        )

    def test_create(self):
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_has_created_at(self):
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'azk4n', unicode(self.obj))

class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        Subscription.objects.create(name='testando o noem', cpf='12345678910',
                                    email='azk5n@null.net', phone='23-33443332')

    def test_cpf_unique(self):
        s = Subscription(name='testando o noem', cpf='12345678910',
                        email='outr@email.com', phone='23-33443332')
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        s = Subscription(name='testando o noem', cpf='12344678910',
                        email='azk5n@null.net', phone='23-33443332')
        self.assertRaises(IntegrityError, s.save)
