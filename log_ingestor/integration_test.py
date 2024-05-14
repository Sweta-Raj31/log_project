from django.test import TestCase, Client

class LogIngestorIntegrationTests(TestCase):
    def test_query_interface(self):
        client = Client()
        response = client.post('/query_interface/', {
            'level': 'info',
            'log_string': 'Test log',
            'source': 'test.log',
            'start_date': '2024-05-01T00:00:00',
            'end_date': '2024-05-31T23:59:59'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Logs found')