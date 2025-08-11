from src.etl.extract import Extracter_corpcodeinfo
from src.etl.transform import Transformer_corpcodeinfo
from src.etl.load import Loader_corpcodeinfo

class Etl_pipeline_corpcodeinfo:

    def execute(self):
        data = Extracter_corpcodeinfo.Extracter_corpcodeinfo().extract()
        Loader_corpcodeinfo.Loader_corpcodeinfo().load(data=data)