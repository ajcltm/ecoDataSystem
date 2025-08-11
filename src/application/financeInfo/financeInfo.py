import pandas as pd
import re
from pathlib import Path
import requests

# CSV 파일 로드
file_path = Path().cwd().joinpath("data","ods","dart","corpcodeinfo.csv")   # CSV 파일 경로
df = pd.read_csv(file_path, encoding="utf-8-sig")
info_key = ["bsns_year", "sj_nm", "account_nm", "thstrm_dt", "thstrm_amount"]

def find_similar_companies_regex(input_name, df, column="corp_name"):
    """
    입력한 값이 포함된 기업명을 찾는 함수
    :param input_name: 사용자가 입력한 기업명
    :param df: 기업명 데이터가 포함된 DataFrame
    :param column: 기업명이 포함된 컬럼명 (기본값: "corp_name")
    :return: 입력값이 포함된 기업명이 포함된 DataFrame
    """
    matched_df = df[df[column].str.contains(re.escape(input_name), regex=True, na=False, case=False)]
    return matched_df

def fetch_corp_info(corp_code):
    """
    OpenDART API를 사용하여 선택한 기업의 정보를 가져오는 함수
    :param corp_code: 기업 코드
    """
    api_key = "YOUR_API_KEY"  # API 키를 입력하세요
    url = f"https://opendart.fss.or.kr/api/fnlttMultiAcnt.json"
    api_key_dart = "52274dad778cf14b88c8a0e18995d7d6929d437b"
    corp_code = corp_code.zfill(8)  # corp_code를 8자리로 맞춤 (앞에 00 추가)
    params = {"crtfc_key":api_key_dart, "corp_code":corp_code, "bsns_year":"2023", "reprt_code":"11011"}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if "list" in data:
            print("기업 정보:")
            for item in data["list"] :
                print("==============================")
                for key, value in item.items():
                    if key in info_key:
                        print(f"{key}: {value}")
        else:
            print("기업 정보를 찾을 수 없습니다.")
    else:
        print("API 요청 실패. 상태 코드:", response.status_code)

if __name__ == "__main__":
    while True:
        user_input = input("기업명을 입력하세요 (종료: exit): ")
        if user_input.lower() == "exit":
            break
        
        result_df = find_similar_companies_regex(user_input, df)
        
        if result_df.empty:
            print("유사한 기업명을 찾을 수 없습니다.")
        elif len(result_df) == 1:
            selected_company = result_df.iloc[0]
            corp_code = str(selected_company['corp_code']).zfill(8)  # corp_code를 8자리로 맞춤
            print(f"선택한 기업: {selected_company['corp_name']}, corp_code: {corp_code}")
            fetch_corp_info(corp_code)
        else:
            print("검색된 기업 목록:")
            for i, row in enumerate(result_df.itertuples(), start=1):
                print(f"{i}. {row.corp_name}")
            
            while True:
                try:
                    selection = int(input("선택할 기업 번호를 입력하세요 (취소: 0): "))
                    if selection == 0:
                        print("선택이 취소되었습니다.")
                        break
                    elif 1 <= selection <= len(result_df):
                        selected_company = result_df.iloc[selection - 1]
                        corp_code = str(selected_company['corp_code']).zfill(8)  # corp_code를 8자리로 맞춤
                        print(f"선택한 기업: {selected_company['corp_name']}, corp_code: {corp_code}")
                        fetch_corp_info(corp_code)
                        break
                    else:
                        print("올바른 번호를 입력하세요.")
                except ValueError:
                    print("숫자를 입력하세요.")