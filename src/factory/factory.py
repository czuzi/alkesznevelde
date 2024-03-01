from src.main_page import getFactoryPage
from src.factory.factory_pages import *
from src.factory.beer import getMadeBeer, startMakeBeer
from src.factory.palinka import getMadePalinka, startMakePalinka

def setAmountToMake(page):
    amountStartString = 'selected="selected">'
    amountStartIndex = page.find(amountStartString) + len(amountStartString)
    amountEndIndex = amountStartIndex + 2
    if page[amountStartIndex+1:amountEndIndex] == '<':
        amountEndIndex = amountStartIndex + 1
    amount = page[amountStartIndex:amountEndIndex]
    print(amount)
    return amount

def getBeersAndStartNewBrew():
    getFactoryPage()
    beerPage = getBeerPage().text
    if beerPage.find('adag sör sikeresen elkészült!'):
        getMadeBeer()
        beerPage = getBeerPage().text
        amount = setAmountToMake(beerPage)
        startMakeBeer(amount)

def getPalinkasAndStartNewBrew():
    getFactoryPage()
    palinkaPage = getPalinkaPage().text
    if palinkaPage.find('adag pálinka sikeresen elkészült!'):
        getMadePalinka()
        palinkaPage = getPalinkaPage().text
        amount = setAmountToMake(palinkaPage)
        startMakePalinka(amount)