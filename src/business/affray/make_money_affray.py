import time
from src.sleep import sleep, wakeUp
from src.main_page import *
from src.business.affray_page import getAffrayPage
from src.business.affray.affray import *
from src.end_process import endProcess
from src.jail import getOutOfJail
from src.common_activities import *

def makeMoneyAffray():
    while True:
        businessPage = getBusinessPage().text
        energy = getEnergy(businessPage)
        printCommonInfo(businessPage)
        takeCareUtils(businessPage)
        decideToGetDrunk = shouldYouGetDrunk(energy, businessPage, 7)
        getOutOfJail()

        if businessPage.find('Jelenleg a Fogdában tartózkodsz gaztettedért!') > -1:
            print("prison")
            time.sleep(10)

        elif businessPage.find('Sajnos elkaptak garázdálkodás közben, 10 percet a fogdán kell töltened') > -1:
            print('go to prison')
            endProcess()
            time.sleep(3)

        elif businessPage.find('A sötét utat választottad: garázdálkodsz!') > -1:
            print("already making money")
            time.sleep(15)

        elif businessPage.find(' kerestél garázdálkodással!') > -1:
            print("end process")
            getMoneyMade(businessPage)
            endProcess()
            time.sleep(2)

        elif energy >= 15 and businessPage.find('Jelenleg a Fogdában tartózkodsz gaztettedért!') == -1 and businessPage.find('Jelenleg az igazak álmát alszod') == -1:
            getBusinessPage()
            getAffrayPage()
            collectProtectionMoney()
            print("money making process started")
            time.sleep(605)
            endProcess()
            time.sleep(2)

        elif energy >= 15 and businessPage.find('Jelenleg az igazak álmát alszod!') > -1:
            wakeUp()
            getBusinessPage()
            getAffrayPage()
            collectProtectionMoney()
            print("woke up and money making process started")
            time.sleep(605)
            endProcess()
            time.sleep(2)

        elif (energy == 14 or energy == 13) and businessPage.find('Jelenleg az igazak álmát alszod!') == -1:
            getMainPage()
            getBusinessPage()
            getMainPage()
            sleep()
            print("low energy, go to sleep")
            time.sleep(15)
        
        elif (energy == 14 or energy == 13) and businessPage.find('Jelenleg az igazak álmát alszod!') > -1:
            print("low energy, sleeping")
            time.sleep(15)

        elif energy >= 10 and businessPage.find('Jelenleg a Fogdában tartózkodsz gaztettedért!') == -1 and businessPage.find('Jelenleg az igazak álmát alszod') == -1:
            getBusinessPage()
            getAffrayPage()
            robbingCashier()
            print("robbing cashier process started")
            time.sleep(425)
            endProcess()
            time.sleep(2)

        elif energy >= 10 and businessPage.find('Jelenleg az igazak álmát alszod!') > -1:
            wakeUp()
            getBusinessPage()
            getAffrayPage()
            robbingCashier()
            print("woke up and robbing cashier  process started")
            time.sleep(425)
            endProcess()

        elif decideToGetDrunk and businessPage.find('Jelenleg az igazak álmát alszod') > -1:
            time.sleep(2)
            wakeUp()
            time.sleep(2)
            getDrunk()

        elif decideToGetDrunk and businessPage.find('Jelenleg az igazak álmát alszod') == -1:
            time.sleep(2)
            getDrunk()

        elif energy < 15 and businessPage.find('Jelenleg az igazak álmát alszod!') == -1:
            getMainPage()
            sleep()
            print("low energy, go to sleep")
            time.sleep(15)

        elif energy < 15 and businessPage.find('Jelenleg az igazak álmát alszod!') > -1:
            print("low energy, sleeping")
            time.sleep(15)

        else:
            print("what else?")
            time.sleep(15)