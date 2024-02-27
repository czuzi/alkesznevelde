import time
from src.sleep import sleep, wakeUp
from src.main_page import *
from src.business.work_page import getWorkPage
from src.business.work.work_activities import physicist
from src.end_process import endProcess
from src.jail import getOutOfJail
from src.common_activities import *

def makeMoneyWork():
    while True:
        businessPage = getBusinessPage().text
        energy = getEnergy(businessPage)
        print(energy)
        money = getMoney(businessPage)
        getDrunkness(businessPage)
        print(getAddiction())
        decideToGetDrunk = shouldYouGetDrunk(energy, businessPage, 7)
        getOutOfJail()

        if businessPage.find('Rájöttél, hogy pénzt keresni kétkezi munkával is lehet!') > -1:
            print("already making money")
            time.sleep(15)

        elif businessPage.find(' kerestél kemény munkával!') > -1:
            print("end process")
            endProcess()

        elif energy >= 13 and businessPage.find('Jelenleg az igazak álmát alszod') == -1:
            getBusinessPage()
            getWorkPage()
            physicist()
            print("money making process started")
            time.sleep(602)
            endProcess()

        elif energy >= 13 and businessPage.find('Jelenleg az igazak álmát alszod!') > -1:
            wakeUp()
            getBusinessPage()
            getWorkPage()
            physicist()
            print("woke up and money making process started")
            time.sleep(602)
            endProcess()

        elif decideToGetDrunk and businessPage.find('Jelenleg az igazak álmát alszod') > -1 and int(money) > 130:
            print('wake up and drink')
            wakeUp()
            getDrunk()

        elif decideToGetDrunk and businessPage.find('Jelenleg az igazak álmát alszod') == -1 and int(money) > 130:
            print('get drunk')
            getDrunk()

        elif businessPage.find('Jelenleg az igazak álmát alszod!') == -1:
            getMainPage()
            sleep()
            print("low energy, go to sleep")
            time.sleep(15)
        
        elif businessPage.find('Jelenleg az igazak álmát alszod!') > -1:
            print("low energy, sleeping")
            time.sleep(15)

        else:
            print("what else?")
            time.sleep(15)