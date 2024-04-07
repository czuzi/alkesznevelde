import time
from src.business.collection.collection_activities import collectingInElite
from src.business.collection_page import getCollectionPage
from src.get_common_data import getAddiction, getDrunkness, getEnergy, getMoney
from src.sleep import sleep, wakeUp
from src.main_page import *
from src.business.work_page import getWorkPage
from src.business.work.work_activities import physicist
from src.business.begging_page import getBeggingPage
from src.business.begging.begging_activities import beggingOnWallStreet
from src.end_process import endProcess
from src.common_activities import *
from src.factory.factory import *

def makeMoneyCollectingSteel():
    while True:
        businessPage = getBusinessPage().text
        energy = getEnergy(businessPage)
        money = getMoney(businessPage)
        printCommonInfo(businessPage)
        takeCareUtils(businessPage)
        
        decideToGetDrunk = shouldYouGetDrunk(energy, businessPage, 7, 'nehezet... vagy értékeset!')

        if businessPage.find('nehezet... vagy értékeset!') > -1:
            print("already collecting steel")
            time.sleep(15)

        elif businessPage.find('Az alábbi "kincseket" találtad fém') > -1:
            print("end process")
            endProcess()

        elif energy >= 8 and businessPage.find('Jelenleg az igazak álmát alszod') == -1:
            getBusinessPage()
            getCollectionPage()
            collectingInElite()
            print("collection in the elite neighborhood")
            time.sleep(482)
            endProcess()

        elif energy >= 8 and businessPage.find('Jelenleg az igazak álmát alszod!') > -1:
            wakeUp()
            getBusinessPage()
            getCollectionPage()
            collectingInElite()
            print("collection in the elite neighborhood")
            time.sleep(482)
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