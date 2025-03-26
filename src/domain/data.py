from dataclasses import dataclass
from typing import List, Any
import pandas as pd

@dataclass
class Corpcode:
    """기업 코드 정보를 담는 데이터 클래스"""
    corpcode: str
    corpname: str
    stockcode: str

    def __str__(self):
        return f"기업코드: {self.corpcode}, 기업명: {self.corpname}, 종목코드: {self.stockcode}"

@dataclass
class Majorcorp:
    """대기업 정보를 담는 데이터 클래스"""
    corpgroup: str
    corpname: str

class Dataset:
    """데이터 인터페이스"""
    def __init__(self):
        self.data: List[Any] = []

    def get_dataframe(self) -> pd.DataFrame:
        """데이터를 DataFrame으로 변환"""
        raise NotImplementedError

class CorpcodeDataset(Dataset):
    """기업 코드 데이터 클래스"""
    def __init__(self, data: List[Corpcode] = None):
        super().__init__()
        self.data = data if data is not None else []

    def get_dataframe(self) -> pd.DataFrame:
        """기업 코드 데이터를 DataFrame으로 변환"""
        records = [
            {
                'corp_code': corp.corpcode,
                'corp_name': corp.corpname,
                'stock_code': corp.stockcode
            }
            for corp in self.data
        ]
        return pd.DataFrame(records)

    def __str__(self) -> str:
        """데이터를 문자열로 변환"""
        if not self.data:
            return "데이터가 없습니다."
        
        result = []
        result.append(f"총 {len(self.data)}개의 기업 데이터")
        result.append("=" * 50)
        
        # 상장/비상장 기업 수 계산
        listed_count = sum(1 for corp in self.data if corp.stockcode)
        unlisted_count = len(self.data) - listed_count
        
        result.append(f"상장 기업: {listed_count}개")
        result.append(f"비상장 기업: {unlisted_count}개")
        result.append("=" * 50)
        
        # 처음 5개 기업의 상세 정보 출력
        result.append("\n[상세 정보]")
        for i, corp in enumerate(self.data[:5], 1):
            result.append(f"{i}. 기업코드: {corp.corpcode}")
            result.append(f"   기업명: {corp.corpname}")
            result.append(f"   종목코드: {corp.stockcode if corp.stockcode else '비상장'}")
            result.append("")
            
        if len(self.data) > 5:
            result.append(f"... 외 {len(self.data) - 5}개")
            
        return "\n".join(result)

    def __repr__(self) -> str:
        """객체의 문자열 표현"""
        return self.__str__()

class MajorcorpDataset(Dataset):
    """대기업 데이터 클래스"""
    def __init__(self, data: List[Majorcorp] = None):
        super().__init__()
        self.data = data if data is not None else []

    def get_dataframe(self) -> pd.DataFrame:
        """대기업 데이터를 DataFrame으로 변환"""
        records = [
            {
                'corp_group': corp.corpgroup,
                'corp_name': corp.corpname
            }
            for corp in self.data
        ]
        return pd.DataFrame(records)

@dataclass
class SaveData:
    """데이터 저장을 위한 클래스"""
    saveNo: int
    data: Dataset 