from django.test import TestCase
from django.core.urlresolvers import reverse
from fbusers.models import FbUserLog


class CreationTest(TestCase):
    def test_list(self):
        response = self.client.get(reverse('person'))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.post(reverse('person'), {'facebookId': '1439785724'})
        self.assertEqual(response.status_code, 201)

    def test_duplicated(self):
        response = self.client.post(reverse('person'), {'facebookId': '1439785724'})
        self.assertEqual(response.status_code, 201)
        response = self.client.post(reverse('person'), {'facebookId': '1439785724'})
        self.assertEqual(response.status_code, 400)

    def test_log(self):
        response = self.client.post(reverse('person'), {'facebookId': '1439785724'})
        self.assertEqual(response.status_code, 201)
        log = FbUserLog.objects.last()
        self.assertEqual(log.facebookId, '1439785724')
        self.assertEqual(log.action, 'created')

    def test_delete(self):
        response = self.client.post(reverse('person'), {'facebookId': '1439785724'})
        self.assertEqual(response.status_code, 201)
        response = self.client.delete(reverse('person_delete', kwargs={'facebookId':'1439785724'}))
        self.assertEqual(response.status_code, 204)
