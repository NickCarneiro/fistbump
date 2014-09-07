import requests

username = 'anned@indeed.com'
password = 'Indeed12'

cookies = {
    'auth_token': 'VyJzHs-fu7zJqy8h9WfyEA',
    '_trajectory_session': 'V01aSC9rbDU2QkovcnVFODdoNXBRazk5U1A2aDZsSUJ5N0E0MVJnVkRmaTltQkpmemZzem5nRnpvUyt6c2lm' +
                           'b1FsemxGU3FsRU1iSXNCNjlQWUtQd0Q1Q3AwamNZckE2V1RDTE1LcjVKM3YwRlF5ZGI4TXEzLy8xc25Fem' +
                           'tTRlAzT256Y2xZYnNCUzAwcEpPUXRjRjlGR0FxVmk5dnRrTDRvek1hRnFxRnhkOHRwdUFqWXVwZ1BTZGV' +
                           'DdDFTL2MwLS1RSTN0TURJY3FZakVuWDJWWHM0Ty93PT0%3D--98a24fc84507faa974d5476f1eaf775' +
                           'ae3a5f037'
}
headers = {
    'X-NewRelic-ID': 'UAIBWF9WGwAAVVBQBwk=',
    'Accept-Encoding': 'gzip,deflate',
    'X-CSRF-Token': 'PG7Xrd1bTxrNBxEk7BipsaKTjkCbiFg4M0Df+3OlE38=',
    'Accept-Language': 'en-US,en;q=0.8,fr;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://app.joinhandshake.com/search',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive'
}

user_ids = []
for page in range(1, 15):
    r = requests.get('https://app.joinhandshake.com/search?utf8=%E2%9C%93&category=User&query=' +
                     '&school_years=4&schools=&majors=&organizations=&skill_names=&graduation_date_minimum=' +
                     '&graduation_date_maximum=&minimum_department_gpa=&maximum_department_gpa='
                     '&minimum_cumulative_gpa=' +
                     '&maximum_cumulative_gpa=&page='+ str(page) +'&sort_column=&sort_direction=',
                     cookies=cookies,
                     headers=headers)
    container = r.json()
    students = container[0]
    for student in students:
        print student['id']






