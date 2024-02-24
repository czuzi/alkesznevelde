import requests

cookies = {
    'logoHide': '1',
    'PHPSESSID': 'ds9vhgiosiul0ktluu9fmsmmj0',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://alkesznevelde.hu/index.php?inc=pub',
    # 'Cookie': 'PHPSESSID=iq2f2k9ukaaolbmhodhngmcni7',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'inc': 'alcohol',
    'pub': '2',
}

def goToLeszVigasz():
    return requests.get('https://alkesznevelde.hu/index.php', params=params, cookies=cookies, headers=headers)