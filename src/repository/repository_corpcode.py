from pathlib import Path
import xml.etree.ElementTree as ET
import pandas as pd

class Repository_corpcode:
    def __init__(self):
        self.path = Path().cwd().joinpath("data", "raw", "dart", "CORPCODE.xml")

    def select_all(self):
        return ET.parse(self.path)