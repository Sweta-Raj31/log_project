from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import LogEntry
from .views import check_logs

class LogEntryModelTests(TestCase):
    def test_log_entry_creation(self):
        log_entry = LogEntry.objects.create(
            level='info',
            log_string='Test log entry',
            source='test.log'
        )
        self.assertIsNotNone(log_entry)
        self.assertEqual(log_entry.level, 'info')
        self.assertEqual(log_entry.log_string, 'Test log entry')
        self.assertEqual(log_entry.source, 'test.log')

class LogIngestorViewTests(TestCase):
    def test_check_logs_view(self):
        request = self.client.post('/check_logs/', {
            'level': 'info',
            'log_string': 'Test log',
            'source': 'test.log',
            'start_date': '2024-05-01T00:00:00',
            'end_date': '2024-05-31T23:59:59'
        })
        self.assertEqual(request.status_code, 200)
        response = request.json()
        self.assertIn('message', response)
        self.assertIn('logs_available', response)


