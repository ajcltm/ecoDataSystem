from abc import ABC, abstractmethod
from src.domain.data import Dataset, CorpcodeDataset
from pathlib import Path

class Loader(ABC):
    """데이터 로더 인터페이스"""
    
    @abstractmethod
    def load(self, dataset: Dataset) -> None:
        """데이터를 로드"""
        pass

class CorpcodeLoader(Loader):
    """기업 코드 로더"""
    def load(self, dataset: CorpcodeDataset) -> None:
        """기업 코드 데이터를 로드"""
        df = dataset.get_dataframe()
        df.to_csv(Path().cwd().joinpath('data', 'raw', 'corpcode.csv'), index=False)
