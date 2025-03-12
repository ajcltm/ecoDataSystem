from src.etl.extract.ods.dart import Extracter_corpcodeinfo
from src.etl.transform.ods.dart import Transformer_corpcodeinfo
from src.etl.load.ods.dart import Loader_corpcodeinfo

class Etl_pipeline_corpcodeinfo:

    def execute(self):
        data = Extracter_corpcodeinfo.Extracter_corpcodeinfo().extract()
        data = Transformer_corpcodeinfo.Transformer_corpcodeinfo().transform(data=data)
        Loader_corpcodeinfo.Loader_corpcodeinfo().load(data=data)