from src.main_page import getFactoryPage
from src.factory.factory_pages import *
from src.factory.beer import getMadeBeer, startMakeBeer
from src.factory.palinka import getMadePalinka, startMakePalinka

def setAmountToMake(beerPage):
    amountStartString = 'selected="selected">'
    amountStartIndex = beerPage.find(amountStartString) + len(amountStartString)
    amountEndIndex = amountStartIndex + 2
    if beerPage[amountStartIndex+1:amountEndIndex] == '<':
        amountEndIndex = amountStartIndex + 1
    amount = beerPage[amountStartIndex:amountEndIndex]
    print(amount)
    return amount

def getBeersAndStartNewBrew():
    getFactoryPage()
    beerPage = getBeerPage().text
    amount = setAmountToMake(beerPage)
    if beerPage.find('adag sör sikeresen elkészült!'):
        getMadeBeer()
        startMakeBeer(amount)

def getPalinkasAndStartNewBrew():
    getFactoryPage()
    palinkaPage = getPalinkaPage().text
    amount = setAmountToMake(palinkaPage)
    if palinkaPage.find('adag pálinka sikeresen elkészült!'):
        getMadePalinka()
        startMakePalinka('20')