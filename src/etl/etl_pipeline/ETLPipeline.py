from src.etl.extract.Extractor import Extractor
from src.etl.transform.Transformer import Transformer
from src.etl.load.Loader import Loader

class ETLPipeline:
    """ETL 파이프라인"""
    def __init__(self, extractor: Extractor, transformer: Transformer, loader: Loader):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def run(self):
        """ETL 파이프라인 실행"""
        dataset = self.extractor.extract()
        transformed_dataset = self.transformer.transform(dataset)
        self.loader.load(transformed_dataset)
