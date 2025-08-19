import unittest
from etl.extract.extracter_stockcorpfnltt import Extracter_stockcorpfnltt


class ExtracterStockCorpFnlttTest(unittest.TestCase):
    def test_extract_data(self):
        extractor = Extracter_stockcorpfnltt()
        data = extractor.extract(dataset="250818_193611 stockcorpfnltt.pkl", target=["00126380", "00164742"])
        valid_data = [d['corp_code'] for d in data if not 'error' in d]
        not_valid_data = [d['corp_code'] for d in data if 'error' in d]
        print(f"Valid corp codes: {valid_data[:3]}... Total: {len(valid_data)}")
        print(f"Not valid corp codes: {not_valid_data[:3]}... Total: {len(not_valid_data)}")

if __name__ == "__main__":
    unittest.main()