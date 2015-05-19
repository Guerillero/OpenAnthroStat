# coding=utf-8
# python 2.X only. If you would like to use 3.X switch fout to 'w' instead of 'wb'.

import config
import csv
import os.path

def average(li, freq):
    sumOf = 0.0
    for i in range(len(li)):
        sumOf = li[i] + sumOf
    return sumOf / freq


def informantparser(s):
    # Remove the first char and return
    st = s[1:]
    return str.strip(st)


def smithS(listOfRanks, listCount, listOfNumbEntries, name):
    # S =(Σ[{L-R+1}/L])/N
    sumOf = 0.0
    for i in range(len(listOfRanks)):
        sumOf = ((listOfNumbEntries[i] - listOfRanks[i] + 1.0) / listOfNumbEntries[i]) + sumOf
    return sumOf / float(listCount)


def sutropS(listOfRanks, freq, listCount):
    # S = F/(N[A])
    # A=(Σ[R])/F
    sumOf = 0.0
    for i in range(len(listOfRanks)):
        sumOf = float(listOfRanks[i]) + sumOf
    return float(freq) / (float(listCount) * (sumOf / float(freq)))


class ItemData:
    def __init__(self, name, rank, entries):
        self.name = name
        self.ranks = []
        self.ranks.append(rank)
        self.totalRanks = []
        self.totalRanks.append(entries)
        self.freq = 1
        self.avRank = average(self.ranks, self.freq)
        self.smith = 0.0
        self.sutrop = 0.0

    def update(self, rank, entries):
        self.ranks.append(rank)
        self.totalRanks.append(entries)
        self.freq = self.freq + 1
        self.avRank = average(self.ranks, self.freq)

    def salience(self, recordCount):
        self.smith = smithS(self.ranks, recordCount, self.totalRanks, self.name)
        self.sutrop = sutropS(self.ranks, self.freq, recordCount)

    def returnData(self):
        newArray = [self.name, self.freq, round(self.avRank, 2), round(self.smith, 4), round(self.sutrop, 4),
                    round((self.smith + self.sutrop) / 2, 4)]
        return newArray


class FreeListData:
    def __init__(self, name):
        self.name = name
        self.FreeList = []

    def addToFL(self, addition):
        self.FreeList.append(addition)

fin = open(config.importFile, 'r')
FreeListMatrix = []

# Turn the  text file into a useful data structure
for line in fin:
    dat = str(line).strip().upper()
    if "#" in dat:
        # if the first char is '#' then it is the name of an informat
        dat = informantparser(dat)
        # create and append a new FreeListData object
        newEntry = FreeListData(dat)
        print(dat)
        FreeListMatrix.append(newEntry)
    else:
        for z in range(len(FreeListMatrix)):
            if z == len(FreeListMatrix)-1:
                if (dat == "") or (dat == " "):
                    "NULL"  # Do nothing
                else:
                    # GOTO the last entry and append to the list of entries in the list
                    FreeListMatrix[z].addToFL(dat)
fin.close()

ItemMatrix = []

for a in range(len(FreeListMatrix)):
    for z in range(len(FreeListMatrix[a].FreeList)):
        listEntry = FreeListMatrix[a].FreeList[z]
        if len(ItemMatrix) == 0:
            ItemMatrix.append(ItemData(listEntry, 1, len(FreeListMatrix[a].FreeList)))
        else:
            for x in range(len(ItemMatrix)):
                if listEntry == ItemMatrix[x].name:
                    ItemMatrix[x].update((z + 1), len(FreeListMatrix[a].FreeList))
                    break
                elif x + 1 == len(ItemMatrix):
                    newItem = ItemData(listEntry, (z + 1), len(FreeListMatrix[a].FreeList))
                    ItemMatrix.append(newItem)
                    break

for x in range(len(ItemMatrix)):
    ItemMatrix[x].salience(len(FreeListMatrix))

fout = open(config.outputFile, 'wb')

csvFile = csv.writer(fout, dialect=csv.excel)
csvFile.writerow(["Name", "Count", "AvRank", "Smith's S", "Sutrop's S", "Aggregate S"])

for x in range(len(ItemMatrix)):
    csvFile.writerow(ItemMatrix[x].returnData())

fout.close()