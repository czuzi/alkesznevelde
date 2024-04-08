import requests
from src.cookies import cookies

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'hu-HU,hu;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://alkesznevelde.hu/index.php?inc=myfactory&id=1',
    
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
}

get_made_wine_params = {
    'inc': 'myfactory',
    'id': '1',
    'action': 'ready',
}

start_make_wine_params = {
    'inc': 'myfactory',
    'id': '1',
    'action': 'work',
}


def getMadeWine():
    return requests.get('https://alkesznevelde.hu/index.php', params=get_made_wine_params, cookies=cookies, headers=headers)

def startMakeWine(amountToMake):
    start_make_wine_data = {
        'count': amountToMake,
        'distSubmit': 'Mehet!',
    }
    return requests.post('https://alkesznevelde.hu/index.php', params=start_make_wine_params, cookies=cookies, headers=headers, data=start_make_wine_data)