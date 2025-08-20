from pathlib import Path

class Loader_stockcorpfnltt:

    def __init__(self):
        self.path = Path().cwd().joinpath("data", "ods", "stockcorpfnltt.csv")

    def load(self, data):
        if data is not None:
            data.to_csv(self.path, encoding="utf-8", index=False)