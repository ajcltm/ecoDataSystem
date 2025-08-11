from pathlib import Path

class Loader_corpcodeinfo:

    def __init__(self):
        self.path = Path().cwd().joinpath("data", "ods", "corpcodeinfo.csv")

    def load(self, data):
        data.to_csv(self.path, encoding="utf-8")