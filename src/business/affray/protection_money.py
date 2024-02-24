import requests

cookies = {
    'logoHide': '1',
    'PHPSESSID': 'ds9vhgiosiul0ktluu9fmsmmj0',
}

start_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'hu-HU,hu;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://alkesznevelde.hu/index.php?inc=affray',
    # 'Cookie': 'logoHide=1; PHPSESSID=ds9vhgiosiul0ktluu9fmsmmj0',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

start_params = {
    'inc': 'affray',
    'geta': '3',
}

robbing_cashier_params = {
    'inc': 'affray',
    'geta': '3',
}

def collectProtectionMoney():
    return requests.get('https://alkesznevelde.hu/index.php', params=start_params, cookies=cookies, headers=start_headers)

def robbingCashier():
    return requests.get('https://alkesznevelde.hu/index.php', params=robbing_cashier_params, cookies=cookies, headers=start_headers)

import requests

cookies = {
    'logoHide': '1',
    'PHPSESSID': 'ds9vhgiosiul0ktluu9fmsmmj0',
}

end_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'hu-HU,hu;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://alkesznevelde.hu/index.php?inc=process',
    # 'Cookie': 'logoHide=1; PHPSESSID=ds9vhgiosiul0ktluu9fmsmmj0',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
}

end_params = {
    'inc': 'process',
    'done': '1',
}

def endCollectProtectionMoney():
    return requests.get('https://alkesznevelde.hu/index.php', params=end_params, cookies=cookies, headers=end_headers)

