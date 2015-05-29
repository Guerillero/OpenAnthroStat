# python 2.X only.

#  The MIT License (MIT)
#
#  Copyright (c) 2015 Tom Fish <guerillero.net>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

from src.common import *
import config
import csv


def main(FreeListMatrix):
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

    # Build the output

    fout = open(config.outputFile, 'wb')

    headings = ["Name", "Count", "AvRank", "Smith's S", "Sutrop's S", "Aggregate S"]

    csvFile = csv.writer(fout, dialect=csv.excel)
    csvFile.writerow(headings)

    for x in range(len(ItemMatrix)):
        csvFile.writerow(ItemMatrix[x].returnData())

    fout.close()

    # Build the text to return to the GUI

    data = ""

    for i in range(len(headings)):
        data += (headings[i] + "\t\t")

    data += "\n"

    for jk in range(1, 100):
        data += "-"

    data += "\n"

    for f in range(len(ItemMatrix)):
        g = ItemMatrix[f].returnData()
        for z in range(len(g)):
            data += (str(g[z]) + "\t\t")
        data += "\n"

    return data
