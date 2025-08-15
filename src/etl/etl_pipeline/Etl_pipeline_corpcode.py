from etl.extract import extracter_corpcode
from etl.load import loader_corpcode

class Etl_pipeline_corpcode:

    def execute(self):
        data = extracter_corpcode.Extracter_corpCode().extract()
        loader_corpcode.Loader_corpcode().load(data=data)