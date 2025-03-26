from abc import ABC, abstractmethod
from typing import Any
import requests
from typing import Dict
import pandas as pd

class DataSource(ABC):
    """데이터 소스 추출기 인터페이스"""
    
    @abstractmethod
    def get_datasource(self) -> Any:
        """데이터 소스에서 데이터를 추출"""
        pass

class APIDataSource(DataSource):
    """API에서 데이터를 추출하는 클래스"""
    
    def __init__(self, url: str, params: Dict[str, Any]):
        self.url = url
        self.params = params

    def get_datasource(self) -> Any:
        """API에서 데이터를 추출"""
        # API 요청
        response = requests.get(self.url, params=self.params)
        
        # 응답 상태 확인
        response.raise_for_status()
        return response.content

class CSVDataSource(DataSource):
    """파일에서 데이터를 추출하는 클래스"""
    
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_datasource(self) -> Any:
        """파일에서 데이터를 추출"""
        return pd.read_csv(self.file_path)
