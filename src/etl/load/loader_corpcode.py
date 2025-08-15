import zipfile
from io import BytesIO
from pathlib import Path

class Loader_corpcode:

    def __init__(self):
        self.path = Path().cwd().joinpath("data", "raw", "dart")

    def load(self, data):
        z = zipfile.ZipFile(BytesIO(data))
        z.extractall(self.path)