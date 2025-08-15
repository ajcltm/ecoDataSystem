import unittest
from etl.extract.extracter_fnltt import Extracter_fnltt

class ExtracterFnlttTest(unittest.TestCase):
    def test_extract_data(self):
        data = Extracter_fnltt().extract(corp_code="00164788")
        print(data)

if __name__ == "__main__":
    unittest.main()