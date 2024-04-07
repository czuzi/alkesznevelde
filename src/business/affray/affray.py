import requests
from src.cookies import cookies

start_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'hu-HU,hu;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://alkesznevelde.hu/index.php?inc=affray',
    
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

collect_protection_money_params = {
    'inc': 'affray',
    'geta': '3',
}

robbing_cashier_params = {
    'inc': 'affray',
    'geta': '2',
}

def collectProtectionMoney():
    return requests.get('https://alkesznevelde.hu/index.php', params=collect_protection_money_params, cookies=cookies, headers=start_headers)

def robbingCashier():
    return requests.get('https://alkesznevelde.hu/index.php', params=robbing_cashier_params, cookies=cookies, headers=start_headers)

