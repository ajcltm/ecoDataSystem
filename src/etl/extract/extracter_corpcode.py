from etl_task.extract.requestor import Requestor
from config import config

class Extracter_corpCode :

    def __init__(self):
        self.url = "https://opendart.fss.or.kr/api/corpCode.xml"
        self.params = {'crtfc_key' : config.api_key_dart}

    def extract(self) :
        data = Requestor().requests(url=self.url, params=self.params, return_type="bytes")
        return data