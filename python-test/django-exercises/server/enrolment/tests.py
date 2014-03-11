from django.test import TestCase
import json
# Create your tests here.

class SchoolTest(TestCase):

    def test_store(self):
        resp = self.client.post('/home',
                                '{"fname":"Leonardo","lname":"Dalla Verde"}',
                                content_type='application/json')
        self.assertEqual(resp.status_code, 200)

    def test_search(self):
        resp = self.client.post('/home',
                                '{"fname":"Leonardo","lname":"Dalla Verde"}',
                                content_type='application/json')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get('/home')

        self.assertEqual(resp.status_code,200)

        content = json.loads(resp.content)

        self.assertEqual(content[0]['fname'], 'Leonardo')
        self.assertEqual(content[0]['lname'], 'Dalla Verde')
        print content[0]['dt']