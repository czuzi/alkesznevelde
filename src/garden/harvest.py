from src.main_page import getGardenPage
from src.garden.harvest_activities import *

def harvest():
    garden = getGardenPage().text

    if garden.find('<a href="index.php?inc=garden&action=collect&id=0">') > -1:
        harvesthops()
        print('hops harvested')

    if garden.find('<a href="index.php?inc=garden&action=collect&id=1">') > -1:
        harvestGrapes()

    if garden.find('<a href="index.php?inc=garden&action=collect&id=2">') > -1:
        harvestPeaches()
        print('peaches harvested')

    if garden.find('<a href="index.php?inc=garden&action=collect&id=3">') > -1:
        harvestPotatoes()
        print('potatoes harvested')
