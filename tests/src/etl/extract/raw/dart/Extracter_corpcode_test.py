import unittest
from src.etl.extract.raw.dart import Extracter_corpcode

class Extracter_corpcode_test(unittest.TestCase):
    def test_extract(self) :
        data = Extracter_corpcode.Extracter_corpCode().extract()
        print(data[:4])

if __name__ == '__main__' :
    unittest.main()