from abc import ABC, abstractmethod
from typing import Any, List
import zipfile
import io
import xml.etree.ElementTree as ET
from .DataSource import DataSource
from src.domain.data import CorpcodeDataset, Corpcode

class Extractor(ABC):
    """데이터 추출기 인터페이스"""

    @abstractmethod
    def parse(self) -> Any:
        """데이터를 파싱"""
        pass
    
    @abstractmethod
    def extract(self) -> Any:
        """데이터를 추출"""
        pass

class CorpcodeExtractor(Extractor):
    """기업 코드 추출기"""
    
    def __init__(self, datasource: DataSource):
        self.datasource = datasource

    def parse(self) -> CorpcodeDataset:
        """XML 데이터를 파싱하여 CorpcodeData 객체로 변환"""
        print("\n1. 데이터 추출")
        raw_data = self.datasource.get_datasource()
            
        # ZIP 파일에서 XML 데이터 추출
        zip_file = zipfile.ZipFile(io.BytesIO(raw_data))
        xml_file = zip_file.namelist()[0]
        print(f"\nZIP 파일 내 파일: {xml_file}")
        
        xml_data = zip_file.read(xml_file)
        
        # XML 파싱
        root = ET.fromstring(xml_data)
        
        # 기업 데이터 리스트 생성
        corp_list = []
        
        # XML 데이터를 Corpcode 객체로 변환
        for list_tag in root.iter('list'):
            corp = Corpcode(
                corpcode=list_tag.find('corp_code').text.strip() if list_tag.find('corp_code') is not None else '',
                corpname=list_tag.find('corp_name').text.strip() if list_tag.find('corp_name') is not None else '',
                stockcode=list_tag.find('stock_code').text.strip() if list_tag.find('stock_code') is not None else ''
            )
            corp_list.append(corp)
        
        # CorpcodeData 객체 생성
        corpcode_data = CorpcodeDataset(data=corp_list)
        return corpcode_data

    def extract(self) -> CorpcodeDataset:
        """데이터를 추출하고 파싱"""
        try:
            return self.parse()
        except Exception as e:
            print(f"Error: 데이터 추출 중 오류 발생: {e}")
            raise