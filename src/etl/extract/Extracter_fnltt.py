from src.config import config
from src.etl_task.extract.Requestor import Requestor

class Extracter_fnltt:

    def __init__(self):
        self.url = f"https://opendart.fss.or.kr/api/fnlttMultiAcnt.json"

    def extract(self, corp_code, bsns_year="2023", reprt_code="11011"):
        params = {"crtfc_key":config.api_key_dart, "corp_code":corp_code, "bsns_year":bsns_year, "reprt_code":reprt_code}
        data = Requestor().requests(url=self.url, params=params, return_type="json")
        return data