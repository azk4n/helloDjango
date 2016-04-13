#coding: utf-8
from django.test import TestCase
from helloDjango.core.models import Speaker, Contact, Talk, Course, Media
from django.core.exceptions import ValidationError
from helloDjango.core.managers import PeriodManager


class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker(name='Fulano de Tal',
                               slug='fulano-de-tal',
                               url='http://meusite.net',
                               description='Example for description!'
                               )
        self.speaker.save()

    def test_create(self):
        'Verifica se instancia de Speaker foi salva'
        self.assertEqual(1, self.speaker.pk)


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            url='http://henriquebastos.net',
            description='Passionate software developer!')

    def test_email(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind='E',
            value='henrique@bastos.net')
        self.assertEqual(1, contact.pk)

    def test_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind='P',
            value='21-96186180')
        self.assertEqual(1, contact.pk)

    def test_fax(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind='F',
            value='21-12345678')
        self.assertEqual(1, contact.pk)

    def test_kind(self):
        'Tipo de contato deve se limitar para E, P ou F.'
        contact = Contact(speaker=self.speaker, value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_unicode(self):
        'Contact string representation should be value'
        contact = Contact(speaker=self.speaker,
                          kind='E',
                          value='henrique@bastos.net')
        self.assertEqual(u'henrique@bastos.net', unicode(contact))


class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title=u'Introdução ao Django',
            description=u'Descrição da palestra.',
            start_time='10:00')

    def test_create(self):
        self.assertEqual(1, self.talk.pk)

    def test_unicode(self):
        self.assertEqual(u'Introdução ao Django', unicode(self.talk))

    def test_speakers(self):
        'Talk tem vários Speakers e vice-versa'
        self.talk.speakers.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            url='http://henriquebastos.net')
        self.assertEqual(1, self.talk.speakers.count())

    def test_period_manager(self):
        'Talk deve ser uma instancia de PeriodManager.'
        self.assertIsInstance(Talk.objects, PeriodManager)

class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title=u'Tutorial Django',
            description=u'Descrição do curso.',
            start_time='10:00', slots=20)

    def test_create(self):
        self.assertEqual(1, self.course.pk)

    def test_unicode(self):
        self.assertEqual(u'Tutorial Django', unicode(self.course))

    def test_speakers(self):
        'Course has many Speakers and vice-versa.'
        self.course.speakers.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            url='http://henriquebastos.net')
        self.assertEqual(1, self.course.speakers.count())

    def test_period_manager(self):
        'Course default manager must be instance of PeriodManager.'
        self.assertIsInstance(Course.objects, PeriodManager)


class MediaModelTest(TestCase):
    def setUp(self):
        t = Talk.objects.create(title='Talk', start_time='11:00')
        self.media = Media.objects.create(talk=t,
                                          kind='Media.YOUTUBE',
                                          media_id='QjxsDd3',
                                          title='Video')
    def test_create(self):
        self.assertEqual(1, self.media.pk)

    def test_unicode(self):
        self.assertEqual('Talk - Video', unicode(self.media))
