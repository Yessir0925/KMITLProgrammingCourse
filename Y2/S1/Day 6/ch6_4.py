def CheckRod(rodA, rodB, rodC, n):
    if n == len(rodA):
        print("|  |  |")

    valA = "|" if rodA[-n] == '0' else rodA[-n]
    valB = "|" if rodB[-n] == '0' else rodB[-n]
    valC = "|" if rodC[-n] == '0' else rodC[-n]

    print(f"{valA}  {valB}  {valC}")

    if n - 1 > 0:
        CheckRod(rodA, rodB, rodC, n - 1)


def SetupRod(rod, n):
    if n <= 0:
        return rod

    rod.append('0')
    return SetupRod(rod, n - 1)


def SetupFirstRod(rod, n):
    return InsertFirstRod(rod, 1, 0, n)


def InsertFirstRod(rod, element, index, end):
    rod[index] = element

    if index + 1 < end:
        return InsertFirstRod(rod, element + 1, index + 1, end)

    return rod


def SolveTower():
    Step(num, rodA, rodC, rodB)


def Step(n, fromRod, toRod, auxRod):
    if n == 0:
        return

    Step(n - 1, fromRod, auxRod, toRod)

    disk = RemoveDisk(fromRod)
    InsertDisk(toRod, disk)

    print(
        "move",
        disk,
        "from ",
        FindRodName(fromRod),
        "to",
        FindRodName(toRod)
    )

    CheckRod(rodA, rodB, rodC, len(rodA))

    Step(n - 1, auxRod, toRod, fromRod)


def RemoveDisk(tower, index=0):
    if tower[index] != '0':
        disk = tower[index]
        tower[index] = '0'
        return disk

    return RemoveDisk(tower, index + 1)

def InsertDisk(tower, disk, index=0):
    if index == len(tower):
        tower[index - 1] = disk
        return tower

    if tower[index] != '0':
        tower[index - 1] = disk
        return tower

    return InsertDisk(tower, disk, index + 1)


def CheckAvailability(n):
    numTower = FindValue(n)
    allTowerIndex = [0, 1, 2]
    allTowerIndex.remove(numTower)

    allTower = [rodA, rodB, rodC]
    availableTower = []

    if CheckTower(allTower[allTowerIndex[0]], n):
        availableTower.append(allTowerIndex[0])

    if CheckTower(allTower[allTowerIndex[1]], n):
        availableTower.append(allTowerIndex[1])

    return availableTower

def CheckTower(tower, disk, index=0):
    if index >= len(tower):
        return True

    if tower[index] != '0':
        return disk < tower[index]

    return CheckTower(tower, disk, index + 1)

def FindValue(n):
    if n in rodA:
        return 0
    elif n in rodB:
        return 1
    elif n in rodC:
        return 2

    return -1


def FindRodName(rod):
    if rod is rodA:
        return "A"
    elif rod is rodB:
        return "B"
    else:
        return "C"


num = int(input("Enter Input : "))

rodA = SetupRod([], num)
rodB = SetupRod([], num)
rodC = SetupRod([], num)

rodA = SetupFirstRod(rodA, num)

CheckRod(rodA, rodB, rodC, len(rodA))

SolveTower()