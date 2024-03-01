import time
from src.pub.leszvigasz_page import goToLeszVigasz
from src.pub.leszvigasz.drink import drinkPalinkaLeszVigasz, drinkBeerLeszVigasz
from src.pub.clan_pub.drink import drinkBeerClanPub
from src.clinic.clinic import getSoberInClinic
from src.puke import puke
from src.sleep import sleep, wakeUp
from src.main_page import *
from src.consume import eatSandwichActivity
from src.garden.harvest import harvest
from src.factory.factory import getBeersAndStartNewBrew, getPalinkasAndStartNewBrew

def getNumberOfSandwiches():
    mainPage = getMainPage().text
    sandwichEndString = ' db</td>'
    sandwichesEndIndex = mainPage.find(sandwichEndString)
    sandwichesStartIndex = sandwichesEndIndex - 2
    if mainPage[sandwichesStartIndex:sandwichesEndIndex-1] == '>':
        sandwichesStartIndex = sandwichesEndIndex - 1
    sandwiches = mainPage[sandwichesStartIndex:sandwichesEndIndex]
    print(sandwiches)
    return sandwiches

def eatSandwich():
    eatSandwichActivity()

def shouldYouGetDrunk(energy, businessPage, maximumEnergy, currentActivity):
    canYouGetDrunk = businessPage.find('perc múlva rúghatsz be!') == -1 and businessPage.find('percen belül újra ihatsz!') == -1 and businessPage.find(currentActivity) == -1
    if energy <= maximumEnergy and canYouGetDrunk:
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
    getMainPage()
    for x in range(2):
        drinkOwnPalinka()
        print('own palinka')
    for x in range(6):
        drinkOwnBeer()
        print('own sor')
    drinkBeerClanPub()
    print('clan beer')
    for x in range(4):
        puke()
        print('puke')

def getAddiction():
    mainPage = getMainPage().text
    addictionStartString = 'részegség minden piából</td><td style="border: 1px double gray;">'
    addictionStartIndex = mainPage.find(addictionStartString) + len(addictionStartString)
    addictionEndIndex = addictionStartIndex + 2
    if mainPage[addictionStartIndex:addictionEndIndex] == '<':
        addictionEndIndex = addictionStartIndex + 3
    addiction = mainPage[addictionStartIndex+1:addictionEndIndex]
    return addiction

def getSober():
    addiction = getAddiction()
    time.sleep(5)
    if int(addiction) > 0:
        getSoberInClinic(addiction)
        print('new addiction')
        print(getAddiction())

def getMoney(businessPage):
    moneyStartString = '<td><b>Pénzed:</b></td><td style="text-align:right;">'
    moneyEndString = ' $</td>'
    moneyStartIndex = businessPage.find(moneyStartString) + len(moneyStartString)
    moneyEndIndex = businessPage.find(moneyEndString)
    money = businessPage[moneyStartIndex:moneyEndIndex]
    print(money)
    return money

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

def harvestAll(businessPage):
    if businessPage.find('color:#00FF00">Kert') > -1:
        harvest()

def collectAndBrew(businessPage):
    if businessPage.find('color:#00FF00">Szesz') > -1:
        getBeersAndStartNewBrew()
        getPalinkasAndStartNewBrew()
