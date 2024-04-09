import requests
from src.cookies import cookies

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'hu-HU,hu;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://alkesznevelde.hu/index.php?inc=jail',
    
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

break_params = {
    'inc': 'jail',
    'akcio': 'break',
}

bail_params = {
    'inc': 'jail',
    'akcio': 'pay',
}

def breakOut():
    return requests.get('https://alkesznevelde.hu/index.php', params=break_params, cookies=cookies, headers=headers)

def bail():
    return requests.get('https://alkesznevelde.hu/index.php', params=bail_params, cookies=cookies, headers=headers)

def braekOrBail():
    response = breakOut().text
    if response.find('Jelenleg a Fogdában tartózkodsz gaztettedért!') > -1:
        print("bailed")
        bail()
    else:
        print("broke")

# cookies = {
#     'PHPSESSID': 'ds9vhgiosiul0ktluu9fmsmmj0',
# }

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#     'Accept-Language': 'hu-HU,hu;q=0.8,en-US;q=0.5,en;q=0.3',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'DNT': '1',
#     'Connection': 'keep-alive',
#     'Referer': 'https://alkesznevelde.hu/index.php?inc=jail',
#     # 'Cookie': 'PHPSESSID=ds9vhgiosiul0ktluu9fmsmmj0',
#     'Upgrade-Insecure-Requests': '1',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     'Sec-GPC': '1',
# }

# params = {
#     'inc': 'jail',
#     'akcio': 'pay',
# }

# response = requests.get('https://alkesznevelde.hu/index.php', params=params, cookies=cookies, headers=headers)