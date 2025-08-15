from etl.extract import extracter_corpcodeinfo
from etl.load import loader_corpcodeinfo

class Etl_pipeline_corpcodeinfo:

    def execute(self):
        data = extracter_corpcodeinfo.Extracter_corpcodeinfo().extract()
        loader_corpcodeinfo.Loader_corpcodeinfo().load(data=data)