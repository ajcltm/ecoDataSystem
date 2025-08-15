import unittest
from etl.extract.extracter_corpcode import Extracter_corpCode
import zipfile
import xml.etree.ElementTree as ET
from io import BytesIO
import os

class Extracter_corpcode_test(unittest.TestCase):

    def test_extract(self):
        # Assuming Extracter_corpcode is defined in the etl.extract module
        data = Extracter_corpCode().extract()
        z = zipfile.ZipFile(BytesIO(data))
        temp_dir = "./src/etl/extract"
        with z as zip_ref:
            zip_ref.extractall(temp_dir)
            print(ET.parse(f"{temp_dir}/CORPCODE.xml"))
        # Clean up extracted files
        if os.path.exists(f"{temp_dir}/CORPCODE.xml"):
            os.remove(f"{temp_dir}/CORPCODE.xml")

if __name__ == "__main__":
    unittest.main()