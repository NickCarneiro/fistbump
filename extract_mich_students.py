import json
import requests
AUTH_TOKEN = 'your auth token cookie'
TRAJECTORY_SESSION = 'your trajectory session cookie'
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

headers = {'If-None-Match': '"01abf23646f5732bc468cb6a9ff77989"',
           'Accept-Encoding': 'gzip,deflate', 'Accept-Language': 'en-US,en;q=0.8,fr;q=0.6',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Referer': 'https://app.joinhandshake.com/search',
           }
cookies = {
    'auth_token': AUTH_TOKEN,
    '_trajectory_session': TRAJECTORY_SESSION
}

f = open('studentids.txt')
student_ids = f.readlines()
for student_id in student_ids:
    student_id = student_id.strip()
    r = requests.get('https://app.joinhandshake.com/users/{}'.format(student_id), cookies=cookies, headers=headers)
    html = r.content
    json_text = find_between(html, 'text/json\'>{"user":', '</script>').replace('text/json\'>', '')
    user_container = json.loads('{"user":' + json_text)
    user = user_container['user']
    educations = user_container['educations']
    for education in educations:
        if 'michigan' in education['school_name'].lower():
            print '{} {} -- {}'.format(user['first_name'], user['last_name'], education['school_name'])
            break
