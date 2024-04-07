import requests

cookies = {
    'PHPSESSID': 'ds9vhgiosiul0ktluu9fmsmmj0',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'hu-HU,hu;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://alkesznevelde.hu/index.php?inc=garden',
    # 'Cookie': 'PHPSESSID=ds9vhgiosiul0ktluu9fmsmmj0',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
}

params = {
    'inc': 'garden',
    'action': 'add',
    'id': '3',
    'num': '1',
}

def plantHops(amountToPlant):
    params = {
        'inc': 'garden',
        'action': 'add',
        'id': '0',
        'num': amountToPlant,
    }
    return requests.get('https://alkesznevelde.hu/index.php', params=params, cookies=cookies, headers=headers)

def plantGrapes(amountToPlant):
    params = {
        'inc': 'garden',
        'action': 'add',
        'id': '1',
        'num': amountToPlant,
    }
    return requests.get('https://alkesznevelde.hu/index.php', params=params, cookies=cookies, headers=headers)

def plantPeaches(amountToPlant):
    params = {
        'inc': 'garden',
        'action': 'add',
        'id': '2',
        'num': amountToPlant,
    }
    return requests.get('https://alkesznevelde.hu/index.php', params=params, cookies=cookies, headers=headers)

def plantPotatoes(amountToPlant):
    params = {
        'inc': 'garden',
        'action': 'add',
        'id': '3',
        'num': amountToPlant,
    }
    return requests.get('https://alkesznevelde.hu/index.php', params=params, cookies=cookies, headers=headers)