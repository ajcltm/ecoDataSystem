from pathlib import Path
import xml.etree.ElementTree as ET
import pandas as pd

class Repository_corpcodeinfo:
    def __init__(self):
        self.path = Path().cwd().joinpath("data", "ods", "corpcodeinfo.csv")

    def select_all(self):
        return pd.read_csv(self.path, encoding="utf-8", dtype={"corp_code": str, "corp_name": str, "stock_code": str})