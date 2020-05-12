import unittest
from unittest.mock import patch

from content.utils import get_meme_url


class TestMeme(unittest.TestCase):
    def test_get_meme_by_id(self):
        with patch('content.utils.requests.get') as mock_get:
            mock_get.return_value.text = "meme"
            data = get_meme_url(1)
        self.assertEqual(data, "https://memasik.ru/memesimages/meme1.jpg")

    def test_get_meme_false_response(self):
        with patch('content.utils.requests.get') as mock_get:
            mock_get.return_value.text = "false"
            data = get_meme_url()
        self.assertEqual(data, '')


if __name__ == '__main__':
    unittest.main()
