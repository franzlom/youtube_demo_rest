import requests
from pprint import pprint


def rest_call_1():
    url = "https://www.googleapis.com/youtube/v3/subscriptions"

    querystring = {"part": "snippet,contentDetails",
                   "channelId": "UC4w_tMnHl6sw5VD93tVymGw",
                   "key": "AIzaSyAqLsuRSNA_va0PiF8ba_r_IVf8_1zJpx8",
                   "maxResults": "50",
                   "regionCode": "NZ"}

    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "2f6219e5-cfba-4d86-97b9-73057f2241bd"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(json.dumps(response.json))

    print(response.json())
    print()
    # pprint(response.json())
    # items = response.json().get('items')
    # print(items)
    for row in response.json().get('items'):
        pprint(row)
        print()
    print('--- page info ---')
    pprint(response.json().get('pageInfo'))

def rest_call_2():
    url = "https://www.googleapis.com/youtube/v3/channels"

    querystring = {"part": "snippet,contentDetails", "id": "UC4w_tMnHl6sw5VD93tVymGw",
                   "key": "AIzaSyAqLsuRSNA_va0PiF8ba_r_IVf8_1zJpx8", "maxResults": "50"}

    headers = {
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

def rest_call_3():
    url = "https://www.googleapis.com/youtube/v3/activities"

    querystring = {"part": "snippet,contentDetails", "channelId": "UCiWLfSweyRNmLpgEHekhoAg",
                   "key": "AIzaSyAqLsuRSNA_va0PiF8ba_r_IVf8_1zJpx8"}

    headers = {

    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    response = requests.request("GET", url, headers=headers, params=querystring)


if __name__== "__main__":
    print('REST CALL 1')
    rest_call_1()

    print('REST CALL 2')
    rest_call_2()

    print('REST CALL 3')
    rest_call_3()