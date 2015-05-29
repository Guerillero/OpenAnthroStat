# coding=utf-8

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


def average(li):
    sumOf = 0.0
    for i in range(len(li)):
        sumOf += li[i]
    return sumOf / len(li)


def informantparser(s):
    # Remove the first char and return
    st = s[1:]
    return str.strip(st)


def smithS(responsePlacement, listCount, freeListLengths):
    # S =(Σ[{L-R+1}/L])/N
    sumOf = 0.0
    for i in range(len(responsePlacement)):
        sumOf = ((freeListLengths[i] - responsePlacement[i] + 1.0) / freeListLengths[i]) + sumOf
    return sumOf / float(listCount)


def sutropS(responsePlacement, listCount):
    # S = F/(N[A])
    # A=(Σ[R])/F
    sumOf = 0.0
    for i in range(len(responsePlacement)):
        sumOf = float(responsePlacement[i]) + sumOf
    return float(len(responsePlacement)) / (float(listCount) * (sumOf / float(len(responsePlacement))))

class ItemData:
    def __init__(self, name, rank, entries):
        self.name = name
        self.ranks = []
        self.ranks.append(rank)
        self.totalRanks = []
        self.totalRanks.append(entries)
        self.freq = 1
        self.avRank = average(self.ranks)
        self.smith = 0.0
        self.sutrop = 0.0

    def update(self, rank, entries):
        self.ranks.append(rank)
        self.totalRanks.append(entries)
        self.freq = self.freq + 1
        self.avRank = average(self.ranks)

    def salience(self, recordCount):
        self.smith = smithS(self.ranks, recordCount, self.totalRanks)
        self.sutrop = sutropS(self.ranks, recordCount)

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

    def returnName(self):
        return self.name

    def returnArray(self):
        return self.FreeList


MIT = "The MIT License (MIT)\n\nCopyright (c) 2015 Tom Fish <guerillero.net>\n\n"
MIT += "Permission is hereby granted, free of charge, to any person obtaining a copy of this software\n" \
       "and associated documentation files (the \"Software\"), to deal in the Software without restriction,\n" \
       "including without limitation the right to use, copy, modify, merge, publish, distribute, sublicense,\n" \
       "and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do\n" \
       "so, subject to the following conditions:\n\n"
MIT += "The above copyright notice and this permission notice shall be included in all copies or substantial\n" \
       "portions of the Software.\n\n"
MIT += "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT\n" \
       "NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY FITNESS FOR A PARTICULAR PURPOSE AND\n" \
       "NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES\n" \
       "OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR\n" \
       "IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."