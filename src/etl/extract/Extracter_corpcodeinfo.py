from pathlib import Path
import xml.etree.ElementTree as ET
from src.repository.Repository_corpcode import Repository_corpcode
import pandas as pd

class Extracter_corpcodeinfo :

    def __init__(self):
        self.path = Path().cwd().joinpath("data", "raw", "dart", "CORPCODE.xml")

    def extract(self) :
        data =  Repository_corpcode().select_all()
        # XML 파싱
    
        root = data.getroot()

        # 첫 번째 레코드를 기준으로 컬럼명 추출
        columns = [elem.tag for elem in root[0]]

        # 데이터 저장
        data = []
        for item in root:
            row = {col: item.find(col).text if item.find(col) is not None else '' for col in columns}
            data.append(row)

        # DataFrame 변환
        df = pd.DataFrame(data)
        return df