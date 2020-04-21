import unittest
from io import StringIO
from unittest.mock import patch

from modules.covid import CovidInfo


class TestCovid(unittest.TestCase):
    def setUp(self) -> None:
        self.covid_info = CovidInfo()

    def test_province_top_not_empty(self):
        with patch('modules.covid.requests.get') as mock_get:
            mock_get.return_value.json.return_value = [{'Confirmed': 1}, {'Confirmed': 2}, {'Confirmed': 3}, {'Confirmed': 4},
                                     {'Confirmed': 5}, {'Confirmed': 6}]
            data = self.covid_info.get_province_top()
        self.assertIsNotNone(data)

    def test_country_top_not_empty(self):
        with patch('modules.covid.requests.get') as mock_get:
            mock_get.return_value.json.return_value = [{"provincestate":"","countryregion":"Co1","lastupdate":"1","confirmed":100000,},{"provincestate":"","countryregion":"Co2","lastupdate":"1","confirmed":100}]
            data = self.covid_info.get_country_top()
        self.assertIsNotNone(data)

    def test_dynamic_top_not_empty(self):
        with patch('modules.covid.requests.get') as mock_get:
            mock_get.return_value.json.return_value = [{"provincestate":"","countryregion":"Co1","timeseries":{"4/18/20":{"confirmed":20},"4/19/20":{"confirmed":10}}}]
            data = self.covid_info.get_dynamic_top()
        self.assertIsNotNone(data)

    def test_get_timeseries_not_empty(self):
        with patch('modules.covid.requests.get') as mock_get:
            mock_get.return_value.json.return_value = [{"provincestate":"","countryregion":"Co1","timeseries":{"4/18/20":{"confirmed":20},"4/19/20":{"confirmed":10}}}]
            data = self.covid_info.get_timeseries()
        self.assertIsNotNone(data)

    def test_get_country_dynamic_top(self):
        with patch('modules.covid.requests.get') as mock_get:
            mock_get.return_value.json.return_value = [{"provincestate":"","countryregion":"Co1","timeseries":{"4/18/20":{"confirmed":20},"4/19/20":{"confirmed":10}}},
                                                       {"provincestate":"","countryregion":"Co2","timeseries":{"4/18/20":{"confirmed":230},"4/19/20":{"confirmed":30}}}]
            data1 = self.covid_info.get_country_dynamic_top(2)
        self.assertNotEqual(len(data1),1)

    def test_get_province_dynamic_top(self):
        with patch('modules.covid.requests.get') as mock_get:
            mock_get.return_value.json.return_value = [{"provincestate":"Can","countryregion":"Co1","timeseries":{"4/18/20":{"confirmed":20},"4/19/20":{"confirmed":10}}},
                                                       {"provincestate":"Can","countryregion":"Co2","timeseries":{"4/18/20":{"confirmed":230},"4/19/20":{"confirmed":30}}}]
            data1 = self.covid_info.get_province_dynamic_top(2)
        self.assertNotEqual(len(data1),1)

    def test_province_country_top_equal(self):
        with patch('modules.covid.requests.get') as mock_get:
            mock_get.return_value.json.return_value = [{"provincestate":"Can","countryregion":"Co1","timeseries":{"4/18/20":{"confirmed":20},"4/19/20":{"confirmed":10}}},
                                                       {"provincestate":"Can","countryregion":"Co2","timeseries":{"4/18/20":{"confirmed":230},"4/19/20":{"confirmed":30}}}]
            data1 = self.covid_info.get_province_dynamic_top(2)
            data2 = self.covid_info.get_country_dynamic_top(2)
        self.assertNotEqual(len(data1),len(data2))


if __name__ == '__main__':
    unittest.main()
