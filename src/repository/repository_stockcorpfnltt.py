from pathlib import Path
import pandas as pd

class Repository_stockcorpfnltt:
    def __init__(self):
        self.path = Path().cwd().joinpath("data", "ods", "stockcorpfnltt.csv")
        self.dtype = {'corp_code':str, 'fs_div':str}
        self.numeric_columns = ['유동자산', '비유동자산', '자산총계', '부채총계', '자본총계', '매출액', '영업이익', '당기순이익', '당기순이익(손실)']

    def select_all(self):
        df = pd.read_csv(self.path, encoding="utf-8", dtype=self.dtype)
        df[self.numeric_columns] = df[self.numeric_columns].round().astype("Int64")
        return df
