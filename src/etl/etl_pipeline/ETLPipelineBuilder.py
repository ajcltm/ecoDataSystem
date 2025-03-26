from src.etl.etl_pipeline.ETLPipeline import ETLPipeline
from src.etl.extract.Extractor import CorpcodeExtractor
from src.etl.transform.Transformer import CorpcodeTransformer
from src.etl.load.Loader import CorpcodeLoader
from src.etl.extract.DataSource import APIDataSource
from src.config.config import API_ENDPOINTS, API_PARAMS

class ETLPipelineBuilder:
    """ETL 파이프라인 빌더"""

    def create_corpcode_pipeline(self) -> ETLPipeline:
        """기업 코드 ETL 파이프라인 생성"""
        datasource = APIDataSource(url=API_ENDPOINTS['corpcode'], params=API_PARAMS['corpcode'])
        corpcode_extractor = CorpcodeExtractor(datasource=datasource)
        corpcode_transformer = CorpcodeTransformer()
        corpcode_loader = CorpcodeLoader()
        return ETLPipeline(corpcode_extractor, corpcode_transformer, corpcode_loader)
