import time
from src.sleep import sleep, wakeUp
from src.main_page import *
from src.business.affray_page import getAffrayPage
from src.business.affray.affray import *
from src.pub.leszvigasz_page import goToLeszVigasz
from src.pub.leszvigasz.drink import drinkPalinkaLeszVigasz, drinkBeerLeszVigasz
from src.clinic.clinic import getSoberInClinic
from src.puke import puke
from src.end_process import endProcess


def shouldYouGetDrunk(energy, businessPage):
    print("prison")
    canYouGetDrunk = businessPage.find('perc múlva rúghatsz be!') == -1 and businessPage.find('perc múlva újra ihatsz') == -1 and businessPage.find('percen belül újra ihatsz!') == -1 and businessPage.find('Jelenleg a Fogdában tartózkodsz gaztettedért!') == -1
    if energy < 8 and canYouGetDrunk:
        return True
    else:
        return False
#  perc múlva rúghatsz be!
def getEnergy(businessPage):
    energyString = '<td><b>Energiád:</b></td><td style="text-align:right;">'
    energyIndex = businessPage.find(energyString) + len(energyString)
    return int(businessPage[energyIndex:energyIndex + 2])

def getDrunk():
    getSober()
    getPubPage()
    goToLeszVigasz()
    for x in range(6):
        drinkPalinkaLeszVigasz()
        print('palinka')
    for x in range(2):
        drinkBeerLeszVigasz()
        print('sor')
    for x in range(4):
        puke()
        print('puke')
    time.sleep(5)

def getSober():
    getClinicPage()
    getSoberInClinic()

def getMoney(businessPage):
    moneyStartString = '<td><b>Pénzed:</b></td><td style="text-align:right;">'
    moneyEndString = ' $</td>'
    moneyStartIndex = businessPage.find(moneyStartString) + len(moneyStartString)
    moneyEndIndex = businessPage.find(moneyEndString)
    money = businessPage[moneyStartIndex:moneyEndIndex]
    print(money)

def getDrunkness(businessPage):
    drunkStartString = '<td><b>Részegséged:</b></td><td style="text-align:right;">'
    drunkEndString = '% <span '
    drunkStartIndex = businessPage.find(drunkStartString) + len(drunkStartString)
    drunkEndIndex = businessPage.find(drunkEndString)
    drunkness = businessPage[drunkStartIndex:drunkEndIndex]
    print(drunkness)

def getMoneyMade(businessPage):
    moneyMadeStartString = 'Összesen <b>'
    moneyMadeEndString = '</b>-t kerestél garázdálkodással!<br />'
    moneyMadeStartIndex = businessPage.find(moneyMadeStartString) + len(moneyMadeStartString)
    moneyMadeEndIndex = businessPage.find(moneyMadeEndString)
    moneyMade = businessPage[moneyMadeStartIndex:moneyMadeEndIndex]
    print(moneyMade)
# Összesen <b>135$</b>-t kerestél garázdálkodással!<br />

def makeMoney():
    while True:
        businessPage = getBusinessPage().text
        energy = getEnergy(businessPage)
        print(energy)
        getMoney(businessPage)
        getDrunkness(businessPage)
        decideToGetDrunk = shouldYouGetDrunk(energy, businessPage)

        if businessPage.find('Jelenleg a Fogdában tartózkodsz gaztettedért!') > -1:
            print(businessPage)
            print("prison")
            time.sleep(10)

        elif businessPage.find('Sajnos elkaptak garázdálkodás közben, 10 percet a fogdán kell töltened') > -1:
            print('go to prison')
            endProcess()
            time.sleep(3)

        elif businessPage.find('A sötét utat választottad: garázdálkodsz!') > -1:
            print("already making money")
            time.sleep(30)

        elif businessPage.find(' kerestél garázdálkodással!') > -1:
            print("end process")
            endProcess()
            time.sleep(2)

        elif energy >= 15 and businessPage.find('Jelenleg a Fogdában tartózkodsz gaztettedért!') == -1 and businessPage.find('Jelenleg az igazak álmát alszod') == -1:
            collectProtectionMoney()
            print("money making process started")
            time.sleep(605)
            endProcess()
            time.sleep(2)

        elif energy >= 15 and businessPage.find('Jelenleg az igazak álmát alszod!') > -1:
            wakeUp()
            collectProtectionMoney()
            print("woke up and money making process started")
            time.sleep(605)
            endProcess()
            time.sleep(2)

        elif (energy == 14 or energy == 13) and businessPage.find('Jelenleg az igazak álmát alszod!') == -1:
            sleep()
            print("low energy, go to sleep")
            time.sleep(30)
        
        elif (energy == 14 or energy == 13) and businessPage.find('Jelenleg az igazak álmát alszod!') > -1:
            print("low energy, sleeping")
            time.sleep(30)

        elif energy >= 10 and businessPage.find('Jelenleg a Fogdában tartózkodsz gaztettedért!') == -1 and businessPage.find('Jelenleg az igazak álmát alszod') == -1:
            robbingCashier()
            print("robbing cashier process started")
            time.sleep(425)
            endProcess()
            time.sleep(5)

        elif energy >= 10 and businessPage.find('Jelenleg az igazak álmát alszod!') > -1:
            wakeUp()
            robbingCashier()
            print("woke up and robbing cashier  process started")
            time.sleep(425)
            time.sleep(5)

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
            time.sleep(30)

        elif energy < 15 and businessPage.find('Jelenleg az igazak álmát alszod!') > -1:
            print("low energy, sleeping")
            time.sleep(30)

        else:
            print("what else?")
            time.sleep(30)