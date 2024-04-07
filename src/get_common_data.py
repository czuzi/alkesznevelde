from src.main_page import getMainPage
from src.safe_actions import getSafeMoneyAmount

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

def getMoney(businessPage):
    moneyStartString = '<td><b>Pénzed:</b></td><td style="text-align:right;">'
    moneyEndString = ' $</td>'
    moneyStartIndex = businessPage.find(moneyStartString) + len(moneyStartString)
    moneyEndIndex = businessPage.find(moneyEndString)
    money = businessPage[moneyStartIndex:moneyEndIndex]
    return money

def getDrunkness(businessPage):
    drunkStartString = '<td><b>Részegséged:</b></td><td style="text-align:right;">'
    drunkEndString = '% <span '
    drunkStartIndex = businessPage.find(drunkStartString) + len(drunkStartString)
    drunkEndIndex = businessPage.find(drunkEndString)
    drunkness = businessPage[drunkStartIndex:drunkEndIndex]
    return drunkness

def getMoneyMade(businessPage):
    moneyMadeStartString = 'Összesen <b>'
    moneyMadeEndString = '</b>-t kerestél garázdálkodással!<br />'
    moneyMadeStartIndex = businessPage.find(moneyMadeStartString) + len(moneyMadeStartString)
    moneyMadeEndIndex = businessPage.find(moneyMadeEndString)
    moneyMade = businessPage[moneyMadeStartIndex:moneyMadeEndIndex]
    print(moneyMade)


def getAddiction():
    mainPage = getMainPage().text
    addictionStartString = 'részegség minden piából</td><td style="border: 1px double gray;">'
    addictionStartIndex = mainPage.find(addictionStartString) + len(addictionStartString)
    addictionEndIndex = addictionStartIndex + 3
    if mainPage[addictionStartIndex+2:addictionEndIndex] == '<':
        addictionEndIndex = addictionStartIndex + 2
    addiction = mainPage[addictionStartIndex+1:addictionEndIndex]
    return addiction

def getEnergy(businessPage):
    energyString = '<td><b>Energiád:</b></td><td style="text-align:right;">'
    energyIndex = businessPage.find(energyString) + len(energyString)
    return int(businessPage[energyIndex:energyIndex + 2])

def getNumberOfOwnBeers():
    mainPage = getMainPage().text
    startString = "Házisör ivása:<br />"
    startIndex = mainPage.find(startString) + len(startString)
    endString = 'onclick="return drink(0)" />'
    endIndex = mainPage.find(endString)
    substring = mainPage[startIndex:endIndex]
    subStartString = '<span style="font-size: 10px;">('
    subStartIndex = substring.find(subStartString) + len(subStartString)
    subEndString = ' házisöröd van)</span></td>'
    subEndIndex = substring.find(subEndString)
    return substring[subStartIndex:subEndIndex]

def getNumberOfOwnPalinkas():
    mainPage = getMainPage().text
    startString = "Házipálesz ivása:<br />"
    startIndex = mainPage.find(startString) + len(startString)
    endString = 'onclick="return drink(2)" />'
    endIndex = mainPage.find(endString)
    substring = mainPage[startIndex:endIndex]
    subStartString = '<span style="font-size: 10px;">('
    subStartIndex = substring.find(subStartString) + len(subStartString)
    subEndString = ' házipáleszed van)</span></td>'
    subEndIndex = substring.find(subEndString)
    return substring[subStartIndex:subEndIndex]

def printCommonInfo(businessPage):
    print(f"energy: {getEnergy(businessPage)}" )
    print(f"drunkness: {getDrunkness(businessPage)}" )
    print(f"money: {getMoney(businessPage)}" )
    print(f"money in the safe: {getSafeMoneyAmount()}")

# def isDrunk():
#     mainPage = getMainPage().text
#     startString = '<td><b>Részegséged:</b></td><td style="text-align:right;">'
#     startIndex = mainPage.find(startString) + len(startString)
#     endString = '% <span style='
#     endIndex  = mainPage.find(endString)