from etl.extract import extracter_stockcorpfnltt
from etl.transform import transformer_stockcorpfnltt
from etl.load import loader_stockcorpfnltt

class Etl_pipeline_stockcorpfnltt:

    def execute(self, dataset=None, bsns_year='2024'):
        data = extracter_stockcorpfnltt.Extracter_stockcorpfnltt().extract(dataset=dataset, bsns_year=bsns_year)
        data = transformer_stockcorpfnltt.Transformer_stockcorpfnltt().transform(data=data)
        loader_stockcorpfnltt.Loader_stockcorpfnltt().load(data=data)