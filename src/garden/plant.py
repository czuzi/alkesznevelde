from variables import hopsNeed, grapesNeed, peachesNeed, potatoesNeed, gardenSize
from src.garden.get_number_of_plants import *
from src.garden.plant_activities import *
from src.main_page import getGardenPage
from src.get_common_data import getMoney
from src.safe_actions import withdraw, getSafeMoneyAmount

def plant():
    gardenPage = getGardenPage().text
    money = int(getMoney(gardenPage))
    numberOfHops = getNumberOfHops(gardenPage)
    numberOfGrapes = getNumberOfGrapes(gardenPage)
    numberOfPeaches = getNumberOfPeaches(gardenPage)
    numberOfPotatoes = getNumberOfPotatoes(gardenPage)
    numberOfAllPlants = numberOfHops + numberOfGrapes + numberOfPeaches + numberOfPotatoes
    canPlant = numberOfAllPlants < gardenSize

    if numberOfHops < hopsNeed and canPlant:
        plantCost = 100
        numberOfNewPlants = {True: hopsNeed - numberOfHops, False: gardenSize - numberOfAllPlants} [hopsNeed - numberOfHops < gardenSize - numberOfAllPlants]
        amountToPlant = calcAmountAndWithdrawCost(plantCost, numberOfNewPlants)
        # numberOfNewPlants = {True: numberOfNewPlants, False: money // 100} [cost < money]
        gardenPage = plantHops(str(amountToPlant))
        numberOfHops += amountToPlant
        numberOfAllPlants += amountToPlant
        canPlant = numberOfAllPlants < gardenSize
        print(f"{amountToPlant} number of hops planted")

    if numberOfGrapes < grapesNeed and canPlant:
        plantCost = 100
        numberOfNewPlants = {True: grapesNeed - numberOfGrapes, False: gardenSize - numberOfAllPlants} [grapesNeed - numberOfGrapes < gardenSize - numberOfAllPlants]
        amountToPlant = calcAmountAndWithdrawCost(plantCost, numberOfNewPlants)
        gardenPage = plantGrapes(str(amountToPlant))
        numberOfGrapes += amountToPlant
        numberOfAllPlants += amountToPlant
        canPlant = numberOfAllPlants < gardenSize
        print(f"{amountToPlant} number of grapes planted")

    if numberOfPeaches < peachesNeed and canPlant:
        plantCost = 200
        numberOfNewPlants = {True: peachesNeed - numberOfPeaches, False: gardenSize - numberOfAllPlants} [peachesNeed - numberOfPeaches < gardenSize - numberOfAllPlants]
        amountToPlant = calcAmountAndWithdrawCost(plantCost, numberOfNewPlants)
        gardenPage = plantPeaches(str(amountToPlant))
        numberOfPeaches += amountToPlant
        numberOfAllPlants += amountToPlant
        canPlant = numberOfAllPlants < gardenSize
        print(f"{amountToPlant} number of peaches planted")

    if numberOfPotatoes < potatoesNeed and canPlant:
        plantCost = 50
        numberOfNewPlants = {True: potatoesNeed - numberOfPotatoes, False: gardenSize - numberOfAllPlants} [potatoesNeed - numberOfPotatoes < gardenSize - numberOfAllPlants]
        amountToPlant = calcAmountAndWithdrawCost(plantCost, numberOfNewPlants)
        gardenPage = plantPotatoes(str(amountToPlant))
        numberOfPotatoes += amountToPlant
        numberOfAllPlants += amountToPlant
        canPlant = numberOfAllPlants < gardenSize
        print(f"{amountToPlant} number of potatoes planted")

def addNewlyPlantedPlants(numberOfHops, numberOfAllPlants, amountToPlant):
    numberOfHops += amountToPlant
    numberOfAllPlants += amountToPlant

def calcAmountAndWithdrawCost(plantCost, numberOfNewPlants):
    amountToPlant = numberOfNewPlants
    moneyInSafe = getSafeMoneyAmount()
    for x in range(numberOfNewPlants):
        cost = amountToPlant * plantCost
        if int(moneyInSafe) >= cost:
            withdraw(str(cost))
            break
        amountToPlant - 1
    return amountToPlant