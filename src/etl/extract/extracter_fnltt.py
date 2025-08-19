from config import config
from etl_task.extract.requestor import Requestor

class Extracter_fnltt:

    def __init__(self):
        self.url = f"https://opendart.fss.or.kr/api/fnlttMultiAcnt.json"

    def fetch(self, corp_code, bsns_year, reprt_code):
        params = {"crtfc_key":config.api_key_dart, "corp_code":corp_code, "bsns_year":bsns_year, "reprt_code":reprt_code}
        data = Requestor().requests(url=self.url, params=params, return_type="json")
        return data
    
    def check_fs_div(self, data):
        for item in data.get("list", []):
            if item.get("fs_div") == "CFS":
                return "CFS"
        return "OFS"
    
    def get_report(self, data, fs_div, corp_code):
        dic = dict()
        dic["corp_code"] = corp_code
        dic["fs_div"] = fs_div
        for item in data.get("list", []):
            if item.get("fs_div") == fs_div:
                key = item.get("account_nm")
                value = item.get("thstrm_amount")
                dic[key] = value
        return dic
    
    def extract(self, corp_code, bsns_year="2024", reprt_code="11011"):
        data = self.fetch(corp_code, bsns_year, reprt_code)
        if data.get("status") == "000":
            fs_div = self.check_fs_div(data)
            return self.get_report(data, fs_div, corp_code)
        else:
            print(f"corp_code: {corp_code} / Error: {data.get('message')}")
            return {"corp_code": corp_code, "error": data.get("message")}