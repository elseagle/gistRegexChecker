import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock


# Mock requests to control its behavior
requests = Mock()

def get_gist():
    r = requests.get('https://api.github.com/gists/public?page=1&per_page=100')
    if r.status_code == 200:
        return r.json()
    return None

class TestLink(unittest.TestCase):
    def test_get_gist_timeout(self):
        # Test a connection timeout
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_gist()


if __name__ == '__main__':
    unittest.main()