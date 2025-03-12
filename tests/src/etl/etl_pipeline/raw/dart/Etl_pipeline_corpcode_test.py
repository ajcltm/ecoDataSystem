import unittest

from src.etl.etl_pipeline.raw.dart import Etl_pipeline_corpcode

class Etl_pipeline_corpcode_test(unittest.TestCase):

    def test_execute(self):
        Etl_pipeline_corpcode.Etl_pipeline_corpcode().execute()

if __name__ == "__main__" :
    unittest.main()