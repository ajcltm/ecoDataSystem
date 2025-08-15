from repository.repository_corpcodeinfo import Repository_corpcodeinfo
from etl.extract.extracter_fnltt import Extracter_fnltt
from etl_task.staging.staging_pickle import save_pickle, load_pickle
from datetime import datetime
from pathlib import Path

import time
import random
import pandas as pd

class Extracter_stockcorpfnltt:

    def __init__(self):
        self.repo = Repository_corpcodeinfo()
        day = datetime.now().strftime("%y%m%d_%H%M%S")
        self.staging_path = Path.cwd().joinpath("data", "stage", f"{day} stockcorpfnltt.pkl")

    def get_target_corpcode(self):
        corp_code_info = self.repo.select_all()
        if not corp_code_info.empty:
            corp_code_info.replace({'stock_code': {r'^\s*$': pd.NA}}, regex=True, inplace=True)
            return corp_code_info[corp_code_info["stock_code"].notnull()]["corp_code"].tolist()
        else:
            print("No corporation code information available.")
            return None

    def extract(self):
        target = self.get_target_corpcode()
        print(f"Target corporation codes: {target[:3]}...")
        target = target[:3]
        target.extend(["00126380", "00164742", "00164788"])
        ex = Extracter_fnltt()

        data = []
        for corp_code in target:
            result = ex.extract(corp_code=corp_code)
            time.sleep(random.randint(1, 3))
            if result:
                data.append(result)
                save_pickle(data, self.staging_path.name)
        pkl = load_pickle(self.staging_path.name)
        print(f"Data loaded from pickle: /n {pkl}")  #
        return pd.DataFrame(data=data) if data else None