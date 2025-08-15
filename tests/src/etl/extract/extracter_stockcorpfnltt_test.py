import unittest
from etl.extract.extracter_stockcorpfnltt import Extracter_stockcorpfnltt


class ExtracterStockCorpFnlttTest(unittest.TestCase):
    def test_extract_data(self):
        extractor = Extracter_stockcorpfnltt()
        data = extractor.extract()
        print(data)

if __name__ == "__main__":
    unittest.main()