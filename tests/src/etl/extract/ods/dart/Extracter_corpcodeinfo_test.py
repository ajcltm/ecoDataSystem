import unittest

from src.etl.extract.ods.dart import Extracter_corpcodeinfo

class Extracter_corpcodeinfo_test(unittest.TestCase):

    def test_extract(self):
        data = Extracter_corpcodeinfo()
        print(data)

if __name__ == "__main__" :
    unittest.main()