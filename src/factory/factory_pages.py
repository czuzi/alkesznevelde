import requests
from src.cookies import cookies

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'hu-HU,hu;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://alkesznevelde.hu/index.php?inc=factory',
    # 'Cookie': 'logoHide=1; PHPSESSID=ds9vhgiosiul0ktluu9fmsmmj0',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
}

beer_page_params = {
    'inc': 'myfactory',
    'id': '0',
}

wine_page_params = {
    'inc': 'myfactory',
    'id': '1',
}

palinka_page_params = {
    'inc': 'myfactory',
    'id': '2',
}

vodka_page_params = {
    'inc': 'myfactory',
    'id': '3',
}

def getBeerPage():
    return requests.get('https://alkesznevelde.hu/index.php', params=beer_page_params, cookies=cookies, headers=headers)

def getWinePage():
    return requests.get('https://alkesznevelde.hu/index.php', params=wine_page_params, cookies=cookies, headers=headers)

def getPalinkaPage():
    return requests.get('https://alkesznevelde.hu/index.php', params=palinka_page_params, cookies=cookies, headers=headers)

def getVodkaPage():
    return requests.get('https://alkesznevelde.hu/index.php', params=vodka_page_params, cookies=cookies, headers=headers)