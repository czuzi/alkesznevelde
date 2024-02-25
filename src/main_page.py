import requests
from src.cookies import cookies

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'hu-HU,hu;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://alkesznevelde.hu/index.php',
    # 'Cookie': 'logoHide=1; PHPSESSID=ds9vhgiosiul0ktluu9fmsmmj0',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
}

main_page_params = {
    'inc': 'data',
}

clinic_params = {
    'inc': 'clinic',
}

pub_params = {
    'inc': 'pub',
}

business_params = {
    'inc': 'business',
}
def getBusinessPage():
    return requests.get('https://alkesznevelde.hu/index.php', params=business_params, cookies=cookies, headers=headers)

def getMainPage():
    return requests.get('https://alkesznevelde.hu/index.php', params=main_page_params, cookies=cookies, headers=headers)

def getClinicPage():
    return requests.get('https://alkesznevelde.hu/index.php', params=clinic_params, cookies=cookies, headers=headers)

def getPubPage():
    return requests.get('https://alkesznevelde.hu/index.php', params=pub_params, cookies=cookies, headers=headers)
