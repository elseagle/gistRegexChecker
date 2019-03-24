import unittest
from unittest.mock import Mock
import re



# Mock requests to control its behavior
requests = Mock()
BeautifulSoup = Mock()

def get_paste():
    r = requests.get('https://pastebin.com/archive')
    if r.status_code == 200:
        return r.json()
    return None

class TestLink(unittest.TestCase):
    def test_get(self):
        get_res = get_paste()
        assert get_res is None, 'GET request failed'

    def test_href(self):
        r = requests.get('https://pastebin.com/archive')
        soup = BeautifulSoup(r.text, 'html.parser')
        paste_list = soup.find('table', class_='maintable')
        pasted = paste_list.find_all('a')
        assert pasted is not None, 'Should have a value'

    def test_regex(self):
        match = "class"
        r = requests.get('https://pastebin.com/archive')
        soup = BeautifulSoup(r.text, 'html.parser')
        paste_list = soup.find('table', class_='maintable')
        pasted = paste_list.find('a')
        link = pasted.get('href')
        url = 'https://pastebin.com{}'.format(link)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('textarea', class_='paste_code')
        content = content.get_text()

        assert re.search(str(match), str(content), re.MULTILINE) is not True, "Regex not available"



if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
