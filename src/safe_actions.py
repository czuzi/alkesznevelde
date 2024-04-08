import requests
from src.cookies import cookies
from src.main_page import getHousePage

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'hu-HU,hu;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://alkesznevelde.hu',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://alkesznevelde.hu/index.php?inc=house',
    # 'Cookie': 'PHPSESSID=ds9vhgiosiul0ktluu9fmsmmj0',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
}

deposit_params = {
    'inc': 'house',
    'action': 'safe_in',
}

withdraw_params = {
    'inc': 'house',
    'action': 'safe_out_some',
}


def deposit(amount):
    data = {
        'betesz': 'Beteszek',
        'betesz_m': amount,
    }

    if int(amount) < 1:
        print("the minimum amount to deposit is 1 dollar")
    else:
        print(f"deposited {amount} dollars")
        return requests.post('https://alkesznevelde.hu/index.php', params=deposit_params, cookies=cookies, headers=headers, data=data)

def withdraw(amount):
    data = {
        'kivesz': 'Kiveszek',
        'kivesz_m': amount,
    }

    if int(amount) < 1:
        print("the minimum amount to withdraw is 1 dollar")
    else:
        print(f"withdrawn {amount} dollars")
        return requests.post('https://alkesznevelde.hu/index.php', params=withdraw_params, cookies=cookies, headers=headers, data=data)

def getSafeMoneyAmount():
    page = getHousePage().text
    startString = 'Széfed: '
    startIndex = page.find(startString) + len(startString)
    endIndex = len(page)
    substring = page[startIndex:endIndex]
    subEndString = ' / '
    subEndIndex = substring.find(subEndString)
    return substring[0:subEndIndex]
