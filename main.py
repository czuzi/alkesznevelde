import time
# from src.business.affley import protection_money
# from src import business_page, main_page, sleep
# from src.business import robbery
# from src.sleep import sleep
from src.sleep import sleep, wakeUp
from src.main_page import *
from src.business.affray_page import getAffrayPage
from src.business.affray.protection_money import collectProtectionMoney, endCollectProtectionMoney

def protectionMoney():
    while True:
        businessPage = getBusinessPage().text

        energyString = '<td><b>Energiád:</b></td><td style="text-align:right;">'

        energyIndex = businessPage.find(energyString) + len(energyString)

        energy = int(businessPage[energyIndex:energyIndex + 2])

        if businessPage.find('A fogdába azok kerülnek, akiknek nem sikerült a Garázdálkodás!') > -1:
            print("prison")
            time.sleep(10)

        elif businessPage.find('A sötét utat választottad: garázdálkodsz!') > -1:
            print("already making money")
            time.sleep(30)

        elif businessPage.find(' kerestél garázdálkodással!') > -1:
            print("end process")
            endCollectProtectionMoney()

        elif energy >= 15 and businessPage.find('A fogdába azok kerülnek, akiknek nem sikerült a Garázdálkodás!') == -1 and businessPage.find('Jelenleg  az igazak álmát alszod') == -1:
            getAffrayPage()
            collectProtectionMoney()
            print("money process started")
            time.sleep(605)
            endCollectProtectionMoney()

        elif energy >= 15 and businessPage.find('Jelenleg  az igazak álmát alszod!') > -1:
            wakeUp()
            getBusinessPage()
            getAffrayPage()
            collectProtectionMoney()
            print("woke up and money process started")
            time.sleep(605)
            endCollectProtectionMoney()

        elif energy < 15 and businessPage.find('Jelenleg  az igazak álmát alszod!') == -1:
            getMainPage()
            sleep()
            print("low energy, go to sleep")
            time.sleep(30)

        elif energy < 15 and businessPage.find('Jelenleg  az igazak álmát alszod!') > -1:
            print("low energy, sleeping")
            time.sleep(30)

        else:
            print("what else?")
            time.sleep(30)

protectionMoney()
