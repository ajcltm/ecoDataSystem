from repository.repository_corpcodeinfo import Repository_corpcodeinfo
from etl.extract.extracter_fnltt import Extracter_fnltt
import time
import random
import pandas as pd
class Extracter_stockcorpfnltt:

    def __init__(self):
        self.repo = Repository_corpcodeinfo()

    def get_target_corpcode(self):
        corp_code_info = self.repo.select_all()
        if not corp_code_info.empty:
            return corp_code_info[corp_code_info["stock_code"].notnull()]["corp_code"].tolist()
        else:
            print("No corporation code information available.")
            return None

    def extract(self):
        target = self.get_target_corpcode()
        print(f"Target corporation codes: {target[:10]}...")
        ex = Extracter_fnltt()

        target = ["00126380", "00164742", "00113526"]

        data = []
        for corp_code in target[:10]:
            result = ex.extract(corp_code=corp_code)
            time.sleep(random.randint(1, 3))
            if result:
                data.append(result)
        return pd.DataFrame(data=data) if data else None