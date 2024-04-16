# Kérlek írd be a képen található szöveget a továbblépéshez:

from time import sleep
from src.common_activities import *
from src.get_common_data import *
from src.main_page import *


def commonActivitiesLoop():
    while True:
        page = getMainPage().text
        energy = getEnergy(page)
        # potatoes = int(getPotatoes())
        # potatoesNeedToEat = 15 - energy
        printCommonInfo(page)
        takeCareUtils(page)
        decideToGetDrunk = shouldYouGetDrunk(energy, page, 42, 'Jelenleg vandálkodsz!')

        if decideToGetDrunk:
            getDrunk()

        else:
            sleep(31)