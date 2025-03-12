import unittest
from src.etl.etl_pipeline.ods.dart import Etl_pipeline_corpcodeinfo

class Etl_pipeline_corpcodeinfo_test(unittest.TestCase):

    def test_execute(self):
        Etl_pipeline_corpcodeinfo.Etl_pipeline_corpcodeinfo().execute()


if __name__ == "__main__" :
    unittest.main()