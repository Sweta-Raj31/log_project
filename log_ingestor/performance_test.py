from locust import HttpUser, between, task

class LogIngestorUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def search_logs(self):
        self.client.post('/query_interface/', {
            'level': 'info',
            'log_string': 'Test log',
            'source': 'test.log',
            'start_date': '2024-05-01T00:00:00',
            'end_date': '2024-05-31T23:59:59'
        })
