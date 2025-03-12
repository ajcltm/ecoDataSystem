from pathlib import Path
import xml.etree.ElementTree as ET

class Extracter_corpcodeinfo :

    def __init__(self):
        self.path = Path().cwd().joinpath("data", "raw", "dart", "CORPCODE.xml")

    def extract(self) :
        return ET.parse(self.path)