import requests
from src.cookies import cookies

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'hu-HU,hu;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://alkesznevelde.hu/index.php?inc=myfactory&id=0',
    
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
}

get_made_beer_params = {
    'inc': 'myfactory',
    'id': '0',
    'action': 'ready',
}

start_make_beer_params = {
    'inc': 'myfactory',
    'id': '0',
    'action': 'work',
}


def getMadeBeer():
    return requests.get('https://alkesznevelde.hu/index.php', params=get_made_beer_params, cookies=cookies, headers=headers)

def startMakeBeer(amountToMake):
    start_make_beer_data = {
        'count': amountToMake,
        'distSubmit': 'Mehet!',
    }
    return requests.post('https://alkesznevelde.hu/index.php', params=start_make_beer_params, cookies=cookies, headers=headers, data=start_make_beer_data)