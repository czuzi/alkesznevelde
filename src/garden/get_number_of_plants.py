def getNumberOfHops(gardenPage):
    startString = '>Komló</td>'
    startIndex = gardenPage.find(startString) + len(startString)
    endString = '>3 óra</td>'
    endIndex = gardenPage.find(endString)
    substring = gardenPage[startIndex:endIndex]
    subStartString = '1px double gray;">'
    subStartIndex = substring.find(subStartString) + len(subStartString)
    subEndString = ' db</td>'
    subEndIndex = substring.find(subEndString)
    return int(substring[subStartIndex:subEndIndex])

def getNumberOfGrapes(gardenPage):
    startString = '>Szõlõ</td>'
    startIndex = gardenPage.find(startString) + len(startString)
    endString = '>2 óra</td>'
    endIndex = gardenPage.find(endString)
    substring = gardenPage[startIndex:endIndex]
    subStartString = '1px double gray;">'
    subStartIndex = substring.find(subStartString) + len(subStartString)
    subEndString = ' db</td>'
    subEndIndex = substring.find(subEndString)
    return int(substring[subStartIndex:subEndIndex])

def getNumberOfPeaches(gardenPage):
    startString = '>Barack</td>'
    startIndex = gardenPage.find(startString) + len(startString)
    endString = '>4 óra</td>'
    endIndex = gardenPage.find(endString)
    substring = gardenPage[startIndex:endIndex]
    subStartString = '1px double gray;">'
    subStartIndex = substring.find(subStartString) + len(subStartString)
    subEndString = ' db</td>'
    subEndIndex = substring.find(subEndString)
    return int(substring[subStartIndex:subEndIndex])

def getNumberOfPotatoes(gardenPage):
    startString = '>Krumpli</td>'
    startIndex = gardenPage.find(startString) + len(startString)
    endString = '>1 óra</td>'
    endIndex = gardenPage.find(endString)
    substring = gardenPage[startIndex:endIndex]
    subStartString = '1px double gray;">'
    subStartIndex = substring.find(subStartString) + len(subStartString)
    subEndString = ' db</td>'
    subEndIndex = substring.find(subEndString)
    return int(substring[subStartIndex:subEndIndex])
