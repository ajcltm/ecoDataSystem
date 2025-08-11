import unittest
from src.etl.etl_pipeline.Etl_pipeline_corpcodeinfo import Etl_pipeline_corpcodeinfo

class EtlPipelineCorpCodeInfoTest(unittest.TestCase):
    
    def test_corp_code_info(self):
        Etl_pipeline_corpcodeinfo().execute()

if __name__ == '__main__':
    unittest.main()