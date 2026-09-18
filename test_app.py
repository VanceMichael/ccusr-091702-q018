import json
import threading
import unittest
import urllib.request
from app import SERVICE_NAME, create_server

class HealthTest(unittest.TestCase):
    def test_health(self):
        server = create_server("127.0.0.1", 0)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{server.server_port}/health") as response:
                self.assertEqual(response.status, 200)
                self.assertEqual(json.load(response), {"status": "ok", "service": SERVICE_NAME})
        finally:
            server.shutdown(); server.server_close(); thread.join()

if __name__ == "__main__": unittest.main()