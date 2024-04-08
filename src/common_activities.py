import time
from src.get_common_data import *
from src.pub.leszvigasz_page import goToLeszVigasz
from src.pub.leszvigasz.drink import drinkPalinkaLeszVigasz, drinkBeerLeszVigasz
from src.pub.clan_pub.drink import drinkBeerClanPub, drinkPalinkaClanPub
from src.clinic.clinic import getSoberInClinic
from src.puke import puke
from src.sleep import sleep, wakeUp
from src.main_page import *
from src.consume import eatSandwichActivity
from src.garden.harvest import harvest
from src.garden.plant import plant
from src.factory.factory import *
from variables import petIds
from src.pet.get_pet_page import getPetPageByPetId
from src.pet.pet_activities import *
from src.safe_actions import deposit, withdraw

def eatSandwich():
    eatSandwichActivity()

def shouldYouGetDrunk(energy, businessPage, maximumEnergy, currentActivity):
    money = int(getMoney(businessPage))
    canYouGetDrunk = businessPage.find('perc múlva rúghatsz be!') == -1 and businessPage.find('percen belül újra ihatsz!') == -1 and businessPage.find(currentActivity) == -1 and money >= 150
    return energy <= maximumEnergy and canYouGetDrunk

    
def shouldYouGetDrunkForVandalism(businessPage, currentActivity):
    money = int(getMoney(businessPage))
    return businessPage.find('perc múlva rúghatsz be!') == -1 and businessPage.find('percen belül újra ihatsz!') == -1 and businessPage.find(currentActivity) == -1 and money >= 150


def getDrunk():

    getSober()
    page = getMainPage()

    for x in range(2):
        if int(getNumberOfOwnPalinkas()) > 0:
            page = drinkOwnPalinka()
            print('own palinka')
        else:
            if int(getMoney(page.text)) > 12:
                page = drinkPalinkaClanPub()
                print("Clan Palinka")
            else:
                print("Not enough money")
                break

    for x in range(4):
        if int(getNumberOfOwnBeers()) > 0:
            page = drinkOwnBeer()
            print('own sor')
        else:
            if int(getMoney(page.text)) > 12:
                page = drinkBeerClanPub()
                print("clan beer")
            else:
                print("Not enough money")
                break

    while int(getDrunkness(page.text)) < 100 and int(getMoney(page.text)) > 12:
        page = drinkPalinkaClanPub()
        print("clan palinka in while loop")
    else:
        if int(getMoney(page.text)) < 13:
            print("not enough money")
        else:
            print("drunk")

    for x in range(4):
        puke()
        print('puke')

def getDrunkForVandalism():
    getSober()
    getMainPage()
    for x in range(1):
        drinkOwnPalinka()
        print('own palinka')
    for x in range(4):
        drinkOwnBeer()
        print('own sor')

def getSober():
    addiction = getAddiction()
    money = int(getMoney(getClinicPage().text))
    if int(addiction) > 0 and money > 50:
        getSoberInClinic(addiction)
        print('new addiction')
        print(getAddiction())

def harvestAll(businessPage):
    if businessPage.find('color:#00FF00">Kert') > -1:
        harvest()

def collectAndBrew(businessPage):
    if businessPage.find('color:#00FF00">Szesz') > -1:
        getBeersAndStartNewBrew()
        getPalinkasAndStartNewBrew()
        getWinesAndStartNewBrew()
        getVodkasAndStartNewBrew()
        

def takeCarePets():
    getMyPetsPage()
    for petId in petIds:
        currentPetPage = getPetPageByPetId(petId).text
        if currentPetPage.find('&action=game">') > -1:
            playWithPetByPetId(petId)
            print(f"played with pet {petId}")
        if currentPetPage.find('&action=food">') > -1:
            feedPetByPetId(petId)
            print(f"fed pet {petId}")

def takeCareUtils(businessPage):
    money = int(getMoney(businessPage))
    plant()
    harvestAll(businessPage)
    collectAndBrew(businessPage)
    takeCarePets()
    if money > 200:
        deposit(str(money - 200))
