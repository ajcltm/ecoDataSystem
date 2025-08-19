from repository.repository_corpcodeinfo import Repository_corpcodeinfo
from etl.extract.extracter_fnltt import Extracter_fnltt
from etl_task.staging.staging_pickle import save_pickle, load_pickle
from datetime import datetime
from pathlib import Path

import time
import random
import pandas as pd
from tqdm import tqdm

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

    def extract(self, dataset=None, target=None):
        if dataset is not None:
            self.staging_path = Path.cwd().joinpath("data", "stage", dataset)
        print(f"Staging path: {self.staging_path}")
        ex_corp_code = []
        ex_dataset = None
        if self.staging_path.exists():
            ex_dataset = load_pickle(self.staging_path.name)
            ex_corp_code = [d['corp_code'] for d in ex_dataset]
            print(f"Existing dataset found with {len(ex_corp_code)} entries.")
        if target is None:
            target = self.get_target_corpcode()
        print(f"Target corporation codes: {target[:3]}... : {len(target)} total")

        ex = Extracter_fnltt()
        data = []
        if ex_dataset is not None:
            data = ex_dataset
        for corp_code in tqdm(target, desc="Extracting data"):
            if corp_code in ex_corp_code:
                # print(f"Data for {corp_code} already exists in staging.")
                continue
            result = ex.extract(corp_code=corp_code)
            time.sleep(random.randint(1, 3))
            if result:
                data.append(result)
                save_pickle(data, self.staging_path.name)
        pkl = load_pickle(self.staging_path.name)
        return pkl