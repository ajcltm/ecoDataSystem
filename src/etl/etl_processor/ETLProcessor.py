from src.etl.etl_pipeline.ETLPipeline import ETLPipeline
from abc import ABC, abstractmethod

class ETLProcessor(ABC):
    """ETL 프로세서"""
    def __init__(self, etl_pipeline: ETLPipeline):
        self.etl_pipeline = etl_pipeline

    @abstractmethod
    def run(self):
        """ETL 프로세서 실행"""
        pass

class CorpcodeETLProcessor(ETLProcessor):
    """기업 코드 ETL 프로세서"""
    def run(self):
        """기업 코드 ETL 프로세서 실행"""
        self.etl_pipeline.run()
