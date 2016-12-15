import cognitive_face as CF
import requests

_BASEURL_ = 'https://api.projectoxford.ai/face/v1.0/'
KEY = open('key.txt', 'rb').readline()
def request(method, url, params, body, headers):
    if not url.startswith('https://'):
        url = _BASEURL_ + url
    if 'Content-Type' not in headers:
        print("컨텐트 타입이 없습니다.")
        headers['Content-Type'] = 'application/json'
    headers['Ocp-Apim-Subscription-Key'] = KEY

    res = requests.request(method, url, params=params, body=body, headers=headers)
    if res.status_code in (200,202):
        result = response.json()

    if res.status_code not in (200,202):
        print("status code : {}".format(res.status_code))
        print("response : {}".format(res.text))
    return result
