import requests
from src.etl.extract.raw.config import config

class Extracter_corpCode :

    def __init__(self):
        self.url = "https://opendart.fss.or.kr/api/corpCode.xml"
        self.params = {'crtfc_key' : config.api_key_dart}

    def extract(self) :
        r = requests.get(url=self.url, params=self.params)
        return r.content
