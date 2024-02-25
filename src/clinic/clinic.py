import requests
from src.cookies import cookies

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://alkesznevelde.hu',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://alkesznevelde.hu/index.php?inc=clinic',
    # 'Cookie': 'PHPSESSID=iq2f2k9ukaaolbmhodhngmcni7',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
}

params = {
    'inc': 'clinic',
    'action': '3',
}

data = {
    'addictionNum': '8',
}

def getSoberInClinic():
    return requests.post('https://alkesznevelde.hu/index.php', params=params, cookies=cookies, headers=headers, data=data)