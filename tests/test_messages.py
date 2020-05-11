import unittest
from unittest.mock import patch

from content import messages


class TestCovidMessage(unittest.TestCase):
    def test_data_found_in_db(self):
        with patch("pymongo.collection.Collection.find_one") as mock_get:
            mock_get.return_value = {'data': [{'countryregion': "US", 'confirmed': 1069424}]}
            data = messages.covid('country_stats', 5)

        self.assertEqual(data.split()[0], "Country")

    def test_data_not_found_db(self):
        with patch("pymongo.collection.Collection.find_one") as mock_get:
            mock_get.return_value = {}

            with patch('content.messages.CovidInfo.get_country_top') as mock2_get:
                mock2_get.return_value = [{'countryregion': "US", 'confirmed': 1069424}]
                data = messages.covid('country_stats', 5)

        self.assertEqual(data.split()[0], "Country")

    def test_data_not_found_in_db_and_not_connection(self):
        with patch("pymongo.collection.Collection.find_one") as mock_get:
            mock_get.return_value = {}

            with patch('content.messages.CovidInfo.get_country_top') as mock2_get:
                mock2_get.return_value = {}
                data = messages.covid('country_stats', 5)

        self.assertEqual(data.split()[0], "Information")


class TestHistoryMessage(unittest.TestCase):
    def test_history_found(self):
        with patch('content.messages.utils.get_history') as mock_get:
            mock_get.return_value = [{'call': 'hello', 'message': 'hello'}]
            data = messages.history(1)
        self.assertEqual(data, 'Action history:\nhello:(hello)\n')

    def test_history_not_found(self):
        with patch('content.messages.utils.get_history') as mock_get:
            mock_get.return_value = []
            data = messages.history(1)
        self.assertEqual(data, "Information not found")


class TestImageRecognitionMessage(unittest.TestCase):
    def test_tags_found(self):
        with patch("content.messages.get_image_tags") as mock_get:
            mock_get.return_value = ['cat']
            data = messages.image_recognition('cat')
        self.assertEqual(data, 'On the picture:\n*cat')

    def test_tags_not_found(self):
        with patch("content.messages.get_image_tags") as mock_get:
            mock_get.return_value = []
            data = messages.image_recognition('cat')
        self.assertEqual(data, "Information not found")


if __name__ == '__main__':
    unittest.main()
