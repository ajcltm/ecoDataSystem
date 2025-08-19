import requests

class Requestor :

    def requests(self, url, params, return_type, method="get"):
        if method == "get" :
            try:
                r = requests.get(url=url, params=params, timeout=10)
            except requests.exceptions.Timeout:
                print("10초 초과, 프로그램 종료")
                sys.exit(1)
        else :
            r = requests.post(url=url, params=params)

        if r.status_code != 200:
            raise Exception(f"Request failed with status code {r.status_code}")

        if return_type == "bytes":
            return r.content
        elif return_type == "json":
            return r.json()
        elif return_type == "text":
            return r.text