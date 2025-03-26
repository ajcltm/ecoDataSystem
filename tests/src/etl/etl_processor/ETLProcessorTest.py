import unittest
from src.etl.etl_processor.ETLProcessor import ETLProcessor, CorpcodeETLProcessor
from src.etl.etl_pipeline.ETLPipelineBuilder import ETLPipelineBuilder

class ETLProcessorTest(unittest.TestCase):
    """ETL 프로세서 테스트"""
    def test_corpcode_etl_processor(self):
        """기업 코드 ETL 프로세서 테스트"""
        builder = ETLPipelineBuilder()
        pipeline = builder.create_corpcode_pipeline()
        processor = CorpcodeETLProcessor(pipeline)
        processor.run()

if __name__ == '__main__':
    unittest.main()


