import unittest
from io import StringIO
from unittest.mock import patch

from modules.content import Cat, CovidInfo, get_image_tags, get_random_meme


class TestCatFact(unittest.TestCase):
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
        self.assertEqual(mock_out.getvalue().strip(),
                         'Error occurred: qqq exception')


class TestCatImage(unittest.TestCase):
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
        self.assertEqual(mock_out.getvalue().strip(),
                         'Error occurred: qqq exception')


class TestMeme(unittest.TestCase):
    def test_ok_request(self):
        with patch('modules.content.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.text = "meme"
            data = get_random_meme()
        self.assertEqual(data, "meme")

    def test_bad_request(self):
        with patch('modules.content.requests.get') as mock_get:
            mock_get.return_value.ok = False
            data = get_random_meme()
        self.assertEqual(data, "Не сегодня...")

    def test_exception_request(self):
        with patch('modules.content.requests.get') as mock_get, patch('sys.stdout', new=StringIO()) as mock_out:
            mock_get.side_effect = Exception('qqq exception')
            get_random_meme()
        self.assertEqual(mock_out.getvalue().strip(),
                         'Error occurred: qqq exception')


class TestCovidCountryTop(unittest.TestCase):
    def test_ok_request(self):
        with patch('modules.content.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = {'iso': "ru"}
            data = CovidInfo.get_country_top()
        self.assertEqual(data, {'iso': "ru"})

    def test_bad_request(self):
        with patch('modules.content.requests.get') as mock_get:
            mock_get.return_value.ok = False
            data = CovidInfo.get_country_top()
        self.assertEqual(data, None)

    def test_exception_request(self):
        with patch('modules.content.requests.get') as mock_get, patch('sys.stdout', new=StringIO()) as mock_out:
            mock_get.side_effect = Exception('qqq exception')
            CovidInfo.get_country_top()
        self.assertEqual(mock_out.getvalue().strip(),
                         'Error occurred: qqq exception')


class TestCovidCountryDynamicTop(unittest.TestCase):
    def test_ok_request(self):
        with patch('modules.content.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = {'iso': "ru"}
            data = CovidInfo.get_country_dynamic_top()
        self.assertEqual(data, {'iso': "ru"})

    def test_bad_request(self):
        with patch('modules.content.requests.get') as mock_get:
            mock_get.return_value.ok = False
            data = CovidInfo.get_country_dynamic_top()
        self.assertEqual(data, None)

    def test_exception_request(self):
        with patch('modules.content.requests.get') as mock_get, patch('sys.stdout', new=StringIO()) as mock_out:
            mock_get.side_effect = Exception('qqq exception')
            CovidInfo.get_country_dynamic_top()
        self.assertEqual(mock_out.getvalue().strip(),
                         'Error occurred: qqq exception')


class TestCovidProvinceTop(unittest.TestCase):
    def test_ok_request(self):
        with patch('modules.content.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = {'iso': "ru"}
            data = CovidInfo.get_province_top()
        self.assertEqual(data, {'iso': "ru"})

    def test_bad_request(self):
        with patch('modules.content.requests.get') as mock_get:
            mock_get.return_value.ok = False
            data = CovidInfo.get_province_top()
        self.assertEqual(data, None)

    def test_exception_request(self):
        with patch('modules.content.requests.get') as mock_get, patch('sys.stdout', new=StringIO()) as mock_out:
            mock_get.side_effect = Exception('qqq exception')
            CovidInfo.get_province_top()
        self.assertEqual(mock_out.getvalue().strip(),
                         'Error occurred: qqq exception')


class TestCovidProvinceDynamicTop(unittest.TestCase):
    def test_ok_request(self):
        with patch('modules.content.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = {'iso': "ru"}
            data = CovidInfo.get_province_dynamic_top()
        self.assertEqual(data, {'iso': "ru"})

    def test_bad_request(self):
        with patch('modules.content.requests.get') as mock_get:
            mock_get.return_value.ok = False
            data = CovidInfo.get_province_dynamic_top()
        self.assertEqual(data, None)

    def test_exception_request(self):
        with patch('modules.content.requests.get') as mock_get, patch('sys.stdout', new=StringIO()) as mock_out:
            mock_get.side_effect = Exception('qqq exception')
            CovidInfo.get_province_dynamic_top()
        self.assertEqual(mock_out.getvalue().strip(),
                         'Error occurred: qqq exception')


class TestImageRecognition(unittest.TestCase):
    def test_ok_request(self):
        with patch('modules.content.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = {'tags': ["hello"]}
            data = get_image_tags("image_url")
        self.assertEqual(data, ["hello"])

    def test_bad_request(self):
        with patch('modules.content.requests.get') as mock_get:
            mock_get.return_value.ok = False
            data = get_image_tags("image_url")
        self.assertEqual(data, None)

    def test_exception_request(self):
        with patch('modules.content.requests.get') as mock_get, patch('sys.stdout', new=StringIO()) as mock_out:
            mock_get.side_effect = Exception('qqq exception')
            get_image_tags("image_url")
        self.assertEqual(mock_out.getvalue().strip(),
                         'Error occurred: qqq exception')


if __name__ == '__main__':
    unittest.main()
