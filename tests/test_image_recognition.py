import unittest
from unittest.mock import patch

from content.web_api import get_image_tags


class TestImageRecognition(unittest.TestCase):
    TEST_URL = 'https://im0-tub-ru.yandex.net/i?id=7eb99aee3b551dd47c63fc636ad6a2e3&n=13&exp=1'

    def test_ok_request(self):
        with patch('content.web_api.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = {'tags': ['hello']}
            data = get_image_tags(TestImageRecognition.TEST_URL)
        self.assertEqual(data, ['hello'])

    def test_invalid_image_url(self):
        with patch('content.web_api.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = {'tags': []}
            data = get_image_tags(TestImageRecognition.TEST_URL)
        self.assertEqual(data, [])

    def test_bad_request(self):
        with patch('content.web_api.requests.get') as mock_get:
            mock_get.return_value.ok = False
            data = get_image_tags(TestImageRecognition.TEST_URL)
        self.assertEqual(data, [])

    def test_exception_request(self):
        with patch('content.utils.requests.get') as mock_get:
            mock_get.side_effect = Exception
            data = get_image_tags(TestImageRecognition.TEST_URL)
        self.assertEqual(data, [])


if __name__ == '__main__':
    unittest.main()
