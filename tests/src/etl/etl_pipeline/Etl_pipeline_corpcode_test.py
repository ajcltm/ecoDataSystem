import unittest

from etl.etl_pipeline import etl_pipeline_corpcode

class Etl_pipeline_corpcode_test(unittest.TestCase):

    def test_execute(self):
        etl_pipeline_corpcode.Etl_pipeline_corpcode().execute()

if __name__ == "__main__" :
    unittest.main()