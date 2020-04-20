import unittest
from unittest.mock import patch
from io import StringIO
from modules.content import Cat


class TestsCatFact(unittest.TestCase):

    def test_ok_request(self):
        with patch('modules.content.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = {'text': 1}
            data = Cat.get_fact()
        self.assertEqual(data, 1)

    def test_bad_request(self):
        with patch('modules.content.requests.get') as mock_get:
            mock_get.return_value.ok = False
            data = Cat.get_fact()
        self.assertEqual(data, None)

    def test_exception_request(self):
        with patch('modules.content.requests.get') as mock_get, patch('sys.stdout', new=StringIO()) as mock_out:
            mock_get.side_effect = Exception('qqq exception')
            Cat.get_fact()
        self.assertEqual(mock_out.getvalue().strip(), 'Error occurred: qqq exception')


class TestsCatImage(unittest.TestCase):

    def test_ok_request(self):
        with patch('modules.content.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = [{"url": 1}]
            data = Cat.get_image()
        self.assertEqual(data, 1)

    def test_bad_request(self):
        with patch('modules.content.requests.get') as mock_get:
            mock_get.return_value.ok = False
            data = Cat.get_image()
        self.assertEqual(data, None)

    def test_exception_request(self):
        with patch('modules.content.requests.get') as mock_get, patch('sys.stdout', new=StringIO()) as mock_out:
            mock_get.side_effect = Exception('qqq exception')
            Cat.get_image()
        self.assertEqual(mock_out.getvalue().strip(), 'Error occurred: qqq exception')

if __name__ == '__main__':
    unittest.main()