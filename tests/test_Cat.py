import unittest
from unittest.mock import patch

from content.Cat import Cat


class TestCatFact(unittest.TestCase):
    def test_ok_request(self):
        with patch('content.utils.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = {'text': 1}
            data = Cat.get_fact()
        self.assertEqual(data, 1)

    def test_bad_request(self):
        with patch('content.utils.requests.get') as mock_get:
            mock_get.return_value.ok = False
            data = Cat.get_fact()
        self.assertEqual(data, None)

    def test_exception_request(self):
        with patch('content.utils.requests.get') as mock_get:
            mock_get.side_effect = Exception
            data = Cat.get_fact()
        self.assertEqual(data, None)


class TestCatImage(unittest.TestCase):
    def test_ok_request(self):
        with patch('content.utils.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = [{"url": 1}]
            data = Cat.get_image()
        self.assertEqual(data, 1)

    def test_bad_request(self):
        with patch('content.utils.requests.get') as mock_get:
            mock_get.return_value.ok = False
            data = Cat.get_image()
        self.assertEqual(data, None)

    def test_exception_request(self):
        with patch('content.utils.requests.get') as mock_get:
            mock_get.side_effect = Exception
            data = Cat.get_fact()
        self.assertEqual(data, None)


if __name__ == '__main__':
    unittest.main()
