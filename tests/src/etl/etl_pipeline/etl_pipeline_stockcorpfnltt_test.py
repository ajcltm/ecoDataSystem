import unittest
from etl.etl_pipeline.etl_pipeline_stockcorpfnltt import Etl_pipeline_stockcorpfnltt
from repository.repository_stockcorpfnltt import Repository_stockcorpfnltt

class EtlPipelineStockCorpFnlttTest(unittest.TestCase):
    
    def test_storkcorpfnltt(self):
        Etl_pipeline_stockcorpfnltt().execute(dataset="250820_125715 stockcorpfnltt_2024.pkl")
        data = Repository_stockcorpfnltt().select_all()
        print(data)

if __name__ == '__main__':
    unittest.main()