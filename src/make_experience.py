import time
from src.business.affray.escape import braekOrBail
from src.get_common_data import getAddiction, getDrunkness, getEnergy, getMoney
from src.main_page import *
from src.end_process import endProcess
from src.jail import getOutOfJail
from src.common_activities import *
from src.business.vandalism.vandalism_activities import getVandalismPage
from src.business.vandalism.vandalism_actions import *
from src.sleep import wakeUp, sleep

def makeExpirience():
    while True:
        businessPage = getBusinessPage().text
        energy = getEnergy(businessPage)
        drunkness = getDrunkness(businessPage)

        printCommonInfo(businessPage)

        if businessPage.find('Kérlek írd be a képen található szöveget a továbblépéshez:') > -1:
            print('captcha :(')
            sleep(41)

        elif businessPage.find('Vandálkodásért járó jutalom:') > -1:
            print('end process')
            endProcess()

        elif businessPage.find('Jelenleg a Fogdában tartózkodsz gaztettedért!') > -1:
            print("prison. break or bail")
            braekOrBail()

        elif businessPage.find('Sajnos elkaptak vandálkodás közben, 10 percet a fogdán kell töltened!') > -1:
            print('go to prison')
            endProcess()

        elif businessPage.find('Jelenleg vandálkodsz!') > -1:
            print("already making experience")
            time.sleep(27)

        elif int(drunkness) >= 30 and energy >= 14 and businessPage.find('Jelenleg az igazak álmát alszod') == -1:
            getBusinessPage()
            getVandalismPage()
            forestVandalism()
            print("vandalism process started")
            time.sleep(902)

        elif int(drunkness) >= 30 and energy >= 14 and businessPage.find('Jelenleg az igazak álmát alszod!') > -1:
            wakeUp()
            getBusinessPage()
            getVandalismPage()
            forestVandalism()
            print("woke up and vandalism process started")
            time.sleep(902)

        elif energy < 14 and businessPage.find('Jelenleg az igazak álmát alszod!') == -1:
            getMainPage()
            sleep()
            print("low energy, go to sleep")
            time.sleep(15)

        elif energy < 14 and businessPage.find('Jelenleg az igazak álmát alszod!') > -1:
            print("low energy, sleeping")
            time.sleep(15)

        else:
            print("what else?")
            time.sleep(15)