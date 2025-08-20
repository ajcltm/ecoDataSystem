from etl_task.staging import staging_pickle
import pandas as pd

class Transformer_stockcorpfnltt():

    def __init__(self):
        self.view_columns = ['corp_code', 'fs_div', 'bsns_year', '유동자산', '비유동자산', '자산총계', '부채총계', '자본총계', '매출액', '영업이익', '당기순이익', '당기순이익(손실)']
        self.numeric_columns = ['bsns_year', '유동자산', '비유동자산', '자산총계', '부채총계', '자본총계', '매출액', '영업이익', '당기순이익', '당기순이익(손실)']
    
    def transform(self, data):
        valid_data = [d for d in data if not "error" in d]
        if not valid_data:
            return None
        valid_df = pd.DataFrame(valid_data)
        vv_df = valid_df[self.view_columns]
        vv_df = vv_df.apply(lambda col: col.str.replace(',', '', regex=True) if col.name in self.numeric_columns else col)
        vv_df = vv_df.apply(lambda col: col.str.replace("-", "", regex=True) if col.name in self.numeric_columns else col)
        for col in self.numeric_columns:
            vv_df[col] = pd.to_numeric(vv_df[col], errors="coerce")
        return vv_df