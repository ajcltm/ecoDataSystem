import xml.etree.ElementTree as ET
import pandas as pd

class Transformer_corpcodeinfo:

    def transform(self, data):
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