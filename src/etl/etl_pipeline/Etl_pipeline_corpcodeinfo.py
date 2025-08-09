from etl.extract import Extracter_corpcodeinfo
from etl.transform import Transformer_corpcodeinfo
from etl.load import Loader_corpcodeinfo

class Etl_pipeline_corpcodeinfo:

    def execute(self):
        data = Extracter_corpcodeinfo.Extracter_corpcodeinfo().extract()
        data = Transformer_corpcodeinfo.Transformer_corpcodeinfo().transform(data=data)
        Loader_corpcodeinfo.Loader_corpcodeinfo().load(data=data)