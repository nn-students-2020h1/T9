import unittest
from unittest.mock import patch

from content import messages


class TestCovidMessage(unittest.TestCase):
    def test_data_found_in_db(self):
        with patch("pymongo.collection.Collection.find_one") as mock_get:
            mock_get.return_value = {'data': [{'countryregion': "US", 'confirmed': 1069424}]}
            data = messages.covid('country_stats', 5)

        self.assertEqual(data.split()[0], "Country")

    @unittest.skip("error on git ci")
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
        with patch('content.messages.get_history') as mock_get:
            mock_get.return_value = [{'call': 'hello', 'message': 'hello'}]
            data = messages.history(1)
        self.assertEqual(data, 'Action history:\nhello:(hello)\n')

    def test_history_not_found(self):
        with patch('content.messages.get_history') as mock_get:
            mock_get.return_value = []
            data = messages.history(1)
        self.assertEqual(data, "Information not found")


class TestImageRecognitionMessage(unittest.TestCase):
    def test_with_tags(self):
        data = messages.image_recognition(['cat'])
        self.assertEqual(data, 'On the picture:\n*cat')

    def test_without_tags(self):
        data = messages.image_recognition([])
        self.assertEqual(data, "Information not found")


class TestWikiMessage(unittest.TestCase):
    def test_data_found(self):
        with patch("content.messages.get_wiki_summary_with_db_check") as mock_wiki:
            mock_wiki.return_value = ('hello', 'hello_url')
            data = messages.wiki_info('hello')
        self.assertEqual(data, 'hello\n\nhello_url')

    def test_data_not_found(self):
        with patch("content.messages.get_wiki_summary_with_db_check") as mock_wiki:
            mock_wiki.return_value = Exception('Test')
            data = messages.wiki_info('hello')
        self.assertEqual(data, 'Information not found. Try again.')


class TestCurrencyRatesMessage(unittest.TestCase):
    def test_data_found(self):
        with patch("content.messages.CurrencyRates.get_currency_rates") as mock_get:
            mock_get.return_value = [('USD', '1')]
            data = messages.currency_rates()
        self.assertEqual(data, 'USD: 1')

    def test_data_not_found(self):
        with patch("content.messages.CurrencyRates.get_currency_rates") as mock_get:
            mock_get.return_value = Exception
            data = messages.currency_rates()
        self.assertEqual(data, 'Information not found.')


if __name__ == '__main__':
    unittest.main()
