import time
from src.sleep import sleep, wakeUp
from src.main_page import *
from src.business.affray_page import getAffrayPage
from src.business.affray.affray import *
from src.business.affray.escape import braekOrBail
from src.end_process import endProcess
from src.jail import getOutOfJail
from src.common_activities import *
from src.consume import eatPotatoes

def potatoGta():
    while True:
        businessPage = getBusinessPage().text
        energy = getEnergy(businessPage)
        potatoes = int(getPotatoes())
        potatoesNeed = 15 - energy
        printCommonInfo(businessPage)
        takeCareUtils(businessPage)
        decideToGetDrunk = shouldYouGetDrunk(energy, businessPage, 15, 'A sötét utat választottad: garázdálkodsz!')

        if businessPage.find('Jelenleg a Fogdában tartózkodsz gaztettedért!') > -1:
            print("prison. break or bail")
            braekOrBail()

        elif businessPage.find('Sajnos elkaptak garázdálkodás közben, 10 percet a fogdán kell töltened') > -1:
            print('go to prison')
            endProcess()

        elif businessPage.find('A sötét utat választottad: garázdálkodsz!') > -1:
            print("already making money")
            time.sleep(15)

        elif businessPage.find(' kerestél garázdálkodással!') > -1:
            print("end process")
            endProcess()

        elif decideToGetDrunk and businessPage.find('Jelenleg az igazak álmát alszod') > -1:
            wakeUp()
            getDrunk()

        elif decideToGetDrunk and businessPage.find('Jelenleg az igazak álmát alszod') == -1:
            getDrunk()

        elif energy >= 15 and businessPage.find('Jelenleg az igazak álmát alszod') == -1:
            getBusinessPage()
            getAffrayPage()
            gta()
            print("money making process started")
            time.sleep(302)
            endProcess()

        elif energy >= 15 and businessPage.find('Jelenleg az igazak álmát alszod!') > -1:
            wakeUp()
            getBusinessPage()
            getAffrayPage()
            gta()
            print("woke up and money making process started")
            time.sleep(302)
            endProcess()

        elif energy < 15 and potatoes > potatoesNeed and businessPage.find('Jelenleg az igazak álmát alszod') == -1:
            eatPotatoes(str(potatoesNeed))
            print(f"{potatoesNeed} potatoes have eaten")

        elif energy < 15 and potatoes > potatoesNeed and businessPage.find('Jelenleg az igazak álmát alszod') == -1:
            wakeUp()
            eatPotatoes(str(potatoesNeed))
            print(f"woke up and {potatoesNeed} potatoes have eaten")

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