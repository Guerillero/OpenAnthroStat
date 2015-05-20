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

def smithS(responsePlacement, listCount, freeListLengths):
    # S =(Σ[{L-R+1}/L])/N
    sumOf = 0.0
    for i in range(len(responsePlacement)):
        sumOf = ((freeListLengths[i] - responsePlacement[i] + 1.0) / freeListLengths[i]) + sumOf
    return sumOf / float(listCount)

# The formula for Smith's S can be found in Smith & Borgatti 1998.
#
# freeListLength: the length of the lists that a response is found in (array of ints)
# responsePlacement: the place in the list that a response was found (array of ints)
#           freeListLength[i] and responsePlacement [i] need to correspond to the same list
# listCount: the total number of lists being analyzed
# returns a float



def sutropS(responsePlacement, listCount):
    # S = F/(N[A])
    # A=(Σ[R])/F
    sumOf = 0.0
    for i in range(len(responsePlacement)):
        sumOf = float(responsePlacement[i]) + sumOf
    return float(len(responsePlacement)) / (float(listCount) * (sumOf / float(len(responsePlacement))))

# The formula for Sutrop's S can be found in Sutrop 2001
#
# responsePlacement: the place in the list that a response was found (array of ints)
# listCount: the total number of lists being analyzed
# returns a float
