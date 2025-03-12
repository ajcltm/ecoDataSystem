from src.etl.extract.raw.dart import Extracter_corpcode
from src.etl.load.raw.dart import Loader_corpcode

class Etl_pipeline_corpcode:

    def execute(self):
        data = Extracter_corpcode.Extracter_corpCode().extract()
        Loader_corpcode.Loader_corpcode().load(data=data)