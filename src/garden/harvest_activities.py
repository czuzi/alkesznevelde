import requests
from src.cookies import cookies

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://alkesznevelde.hu/index.php?inc=garden',
    # 'Cookie': 'PHPSESSID=iq2f2k9ukaaolbmhodhngmcni7',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
}

harvest_hop_params = {
    'inc': 'garden',
    'action': 'collect',
    'id': '0',
}

harvest_grapes_params = {
    'inc': 'garden',
    'action': 'collect',
    'id': '1',
}

harvest_peach_params = {
    'inc': 'garden',
    'action': 'collect',
    'id': '2',
}

harvest_potato_params = {
    'inc': 'garden',
    'action': 'collect',
    'id': '3',
}

def harvesthops():
    return requests.get('https://alkesznevelde.hu/index.php', params=harvest_hop_params, cookies=cookies, headers=headers)

def harvestGrapes():
    return requests.get('https://alkesznevelde.hu/index.php', params=harvest_grapes_params, cookies=cookies, headers=headers)

def harvestPeaches():
    return requests.get('https://alkesznevelde.hu/index.php', params=harvest_peach_params, cookies=cookies, headers=headers)

def harvestPotatoes():
    return requests.get('https://alkesznevelde.hu/index.php', params=harvest_potato_params, cookies=cookies, headers=headers)