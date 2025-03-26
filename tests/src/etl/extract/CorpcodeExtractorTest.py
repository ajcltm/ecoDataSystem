import unittest
import xml.etree.ElementTree as ET
from src.etl.extract.DataSource import APIDataSource
from src.etl.extract.Extractor import CorpCodeExtractor
from src.config.config import API_ENDPOINTS, API_PARAMS

class TestCorpcodeExtractor(unittest.TestCase):
    def setUp(self):
        """테스트 설정"""
        self.datasource = APIDataSource(url=API_ENDPOINTS['corpcode'], params=API_PARAMS['corpcode'])
        self.extractor = CorpCodeExtractor(datasource=self.datasource)

    def test_extract(self):
        print(self.extractor.extract())
            

if __name__ == '__main__':
    unittest.main()
