import unittest
from unittest.mock import patch

from content.micro import get_random_meme


class TestMeme(unittest.TestCase):
    def test_ok_request(self):
        with patch('content.utils.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = "meme"
            data = get_random_meme()
        self.assertEqual(data, "meme")

    def test_bad_request(self):
        with patch('content.utils.requests.get') as mock_get:
            mock_get.return_value.ok = False
            data = get_random_meme()
        self.assertEqual(data, None)

    def test_exception_request(self):
        with patch('content.utils.requests.get') as mock_get:
            mock_get.side_effect = Exception
            data = get_random_meme()
        self.assertEqual(data, None)


if __name__ == '__main__':
    unittest.main()
