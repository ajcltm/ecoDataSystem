import unittest
from etl.extract.extracter_stockcorpfnltt import Extracter_stockcorpfnltt


class ExtracterStockCorpFnlttTest(unittest.TestCase):
    def test_extract_data(self):
        extractor = Extracter_stockcorpfnltt()
        # data = extractor.extract(dataset="250818_193611 stockcorpfnltt.pkl", target=["00126380", "00164742"])
        data = extractor.extract(dataset="250818_193611 stockcorpfnltt.pkl")
        valid_data = [d for d in data if not 'error' in d]
        valid_corpcode = [d['corp_code'] for d in data if not 'error' in d]
        not_valid_data = [d['corp_code'] for d in data if 'error' in d]
        print(f"Valid corp codes: {valid_corpcode[:3]}... Total: {len(valid_corpcode)}")
        print(f"Valid data sample: corp_code: {valid_data[0]['corp_code']} / 매출액: {valid_data[0]['매출액']}")
        print(f"Not valid corp codes: {not_valid_data[:3]}... Total: {len(not_valid_data)}")

if __name__ == "__main__":
    unittest.main()