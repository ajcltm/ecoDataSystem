import unittest
from src.etl.extract.Extracter_fnltt import Extracter_fnltt

class ExtracterFnlttTest(unittest.TestCase):
    def test_extract_data(self):
        data = Extracter_fnltt().extract(corp_code="00126380")
        print(data)

if __name__ == "__main__":
    unittest.main()