import requests
import json
from datetime import datetime
from datetime import date
import pandas as pd
from bs4 import BeautifulSoup
import re


def description(input) -> str:

    soup = BeautifulSoup(input, features="html.parser").get_text()
    soup = soup.replace("\xa0", " ")
    soup = soup.replace("\n", " ")
    return soup

today = date.today()
print(today)
url = f"https://rutgers.campuslabs.com/engage/api/discovery/event/search?endsAfter={today}T15%3A28%3A19-04%3A00&orderByField=endsOn&orderByDirection=ascending&status=Approved&take=50&benefitNames%5B0%5D=FreeFood&query=&skip=0"
payload = {}
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'JSESSIONID=A778C5AA2FF557421AAA19088F7278C8.soc; fpestid=TVRnUoLQyeBZquD2gXJg8BB2rzrz1VZmR_5II83Q7UmxgkD7zf2yuuGzASnSfAyDnytgcQ; _rollupga=GA1.2.2132069169.1662607485; _ga_CF2ZXYSNT3=GS1.1.1664844634.2.0.1664844634.0.0.0; _hjSessionUser_3158812=eyJpZCI6ImJlM2E2MDhhLTgxZWYtNTFhMS05ZGQ2LTQ1MjVmZTc0OTcwNyIsImNyZWF0ZWQiOjE2NjYwNDU5NjYzNDIsImV4aXN0aW5nIjp0cnVlfQ==; _cc_id=bf7b61fbc2041492177919704b7cea65; _hjSessionUser_1294944=eyJpZCI6IjM5MGViYWU1LThlMWUtNTk0Ni04ZjE0LTQyN2FhMWFiZDQ2YyIsImNyZWF0ZWQiOjE2NjU0MzA4NjcwOTgsImV4aXN0aW5nIjp0cnVlfQ==; _ga_X4L8E18CVL=GS1.1.1668527798.1.1.1668527811.0.0.0; _ga_Z6199W0J4R=GS1.1.1668530082.2.0.1668530092.0.0.0; _hjSessionUser_3231770=eyJpZCI6ImY3NzY5M2VjLTllNWEtNTc5ZC05Njc4LWU5NGJmM2I5NjhlZCIsImNyZWF0ZWQiOjE2Njg4MDUyMDI4NDAsImV4aXN0aW5nIjp0cnVlfQ==; _clck=prznhg|1|f70|0; _scid=8a91642d-e390-4292-b07c-1b43fe0f4155; _tt_enable_cookie=1; _ttp=d2d845ca-2da6-4a9d-87d9-0b64bba34137; _ga_MLYZ1CRP7C=GS1.1.1669851793.1.1.1669851969.60.0.0; _ga_RKQ079HYFR=GS1.1.1671131327.1.0.1671131341.0.0.0; _ga_CM7R76EQQN=GS1.1.1671131245.2.1.1671131454.0.0.0; _hjSessionUser_2593350=eyJpZCI6IjhkYWNkMTYyLTQ0ZTUtNThmZC04YWRhLTM3Y2U5OGI2MDE3YiIsImNyZWF0ZWQiOjE2NzE1ODY2MzUxMDEsImV4aXN0aW5nIjp0cnVlfQ==; _ga_T2SXJM5L7G=GS1.1.1671595540.2.1.1671595575.0.0.0; _ga_K7N8GCP9CJ=GS1.1.1673395217.2.0.1673395218.0.0.0; _ga_NQ7HLJ30E3=GS1.1.1673429263.6.0.1673429263.0.0.0; _ga_0SP8PB5CPS=GS1.1.1673773739.5.1.1673773838.0.0.0; _ga_C9TCE1C461=GS1.1.1674452203.23.1.1674453278.0.0.0; _ga_4BJDT7REEF=GS1.1.1675284807.2.0.1675284807.0.0.0; _uetvid=54ee4870a28211ed80cb43dda0057852; _ce.s=v~c418829e9c1fd3aeb54db63da78ad8bda452fa6c~vpv~0~v11.rlc~1675291617742; _ga_V859C9HTED=GS1.1.1675804107.1.0.1675804112.0.0.0; _ga_FJJ06ZV9LX=GS1.1.1676415075.13.0.1676415099.0.0.0; _ga_B6BCKQE1XW=GS1.1.1676927245.8.1.1676927456.0.0.0; _ga_N90882N2TY=GS1.1.1677520254.1.0.1677520254.0.0.0; _ga_C6VL55M96K=GS1.1.1677622976.5.0.1677622976.0.0.0; _ga_DVCN4VQT8D=GS1.1.1678658223.1.0.1678658225.0.0.0; _ga_KMRD2XMMJR=GS1.1.1679420270.2.0.1679420270.0.0.0; _ga_00V39HKZPH=GS1.1.1679522317.1.0.1679522324.0.0.0; _ga=GA1.2.2132069169.1662607485; visid_incap_2811896=qqprrGNsRwSgcgGYeJmCh2UNrmQAAAAAQUIPAAAAAACNrfumAr/b+Z00LrFD2as+; ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%22189225943831ef2-065f68c91f5861-1b525634-13c680-18922594384e91%22%2C%22%24device_id%22%3A%22189225943831ef2-065f68c91f5861-1b525634-13c680-18922594384e91%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; EssUserTrk=7dfc31ba.602d3e5f48af5; sis-content=1122770348.20480.0000; sis-soc=1156324780.20480.0000; sascas_4_envelope_79=007335107841861692211059; nsoToken=AlsMwc4aB6iO%2B38IQWW7jC7h9wHxMr1B7ams5FEibnUSZms0M6hJyJ%2FcX9V96I1X; loginNetId=yis11; ARRAffinity=4b4257cd45f53819c8629bee4b57736a2918ec7b765d9ce150fadd8a474c9700; ARRAffinitySameSite=4b4257cd45f53819c8629bee4b57736a2918ec7b765d9ce150fadd8a474c9700',
    'If-None-Match': '2054787009',
    'Referer': 'https://sis.rutgers.edu/soc/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"'
}
response = (requests.request("GET", url, headers=headers, data=payload)).json()
url = f"https://rutgers.campuslabs.com/engage/api/discovery/event/search?endsAfter={today}T15%3A28%3A19-04%3A00&orderByField=endsOn&orderByDirection=ascending&status=Approved&take={response['@odata.count']}&benefitNames%5B0%5D=FreeFood&query=&skip=0"
response = (requests.request("GET", url, headers=headers, data=payload)).json()
rows = [event for event in response['value']]
df = pd.DataFrame(rows)
print(df)
df['startsOn'] = pd.to_datetime(df['startsOn'])
df['endsOn'] = pd.to_datetime(df['endsOn'])
df['startsOn'] = df['startsOn'].dt.strftime('%Y-%m-%d %I:%M %p')
df['endsOn'] = df['endsOn'].dt.strftime('%I:%M %p')

df["description"] = df["description"].map(description)

with open("src/assets/data.json", "w") as file:
    unformatted = json.loads(df.to_json(orient="table"))
    json.dump(unformatted['data'], file, indent=4, sort_keys=True)
