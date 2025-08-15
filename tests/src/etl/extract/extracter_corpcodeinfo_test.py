import unittest
from etl.extract.extracter_corpcodeinfo import Extracter_corpcodeinfo

class Extracter_corpcodeinfo_test(unittest.TestCase):

    def test_extract(self):
        data = Extracter_corpcodeinfo().extract()
        print(data)

if __name__ == "__main__" :
    unittest.main()