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

class flEntry:
    def __init__(self, name):
        self.name = name
        self.chain = []

    def addRank(self, rank):
        self.chain.append(rank)

    def returnData(self):
        return self.chain

def main(FreelistdataArray):
    print(FreelistdataArray)
    matrix = []
    inf = []
    for i in range(len(FreelistdataArray)):
        fla = FreelistdataArray[i].returnArray()
        inf.append(FreelistdataArray[i].returnName())
        for x in range(len(fla)):
            if len(matrix) == 0:
                newbie = flEntry(fla[x])
                matrix.append(newbie)
            else:
                for z in range(len(matrix)):
                    if matrix[z].name == fla[x]:
                        break
                    elif x + 1 == len(matrix):
                        matrix.append(flEntry(fla[x]))
                        break
    for v in range(len(FreelistdataArray)):
        for q in range(len(FreelistdataArray[v].FreeList)):
            for b in range(len(matrix)):
                print(str(len(FreelistdataArray[v].FreeList)) + " : " +str(q))
                if matrix[b].name == FreelistdataArray[v].FreeList[q]:
                    matrix[b].addRank(q+1)
                    break
                elif len(FreelistdataArray[v].FreeList) == q+1:
                    matrix[b].addRank(0)
                    break
    for c in range(len(matrix)):
        print(matrix[c].name + "\t\t" + str(matrix[c].returnData()))
    print("end")