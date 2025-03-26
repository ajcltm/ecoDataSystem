from abc import ABC, abstractmethod
from ...domain.data import Dataset, CorpcodeDataset

class Transformer(ABC):
    """데이터 변환기 인터페이스"""
    
    @abstractmethod
    def transform(self, dataset: Dataset) -> Dataset:
        """데이터를 변환"""
        pass

class CorpcodeTransformer(Transformer):
    """기업 코드 변환기"""
    
    def transform(self, dataset: CorpcodeDataset) -> CorpcodeDataset:
        """기업 코드 데이터를 변환"""
        return dataset

