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

from Tkinter import *
from main import *
import tkFileDialog as tkFD
import config


def inputChooser():
        config.importFile = tkFD.askopenfilename()


def outputChooser():
        config.outputFile = tkFD.askopenfilename()


def launcher():
    outputs = main()

    #update the text
    tex.insert(END, outputs)

    # join
    sb.config(command=tex.yview)
    tex.config(yscrollcommand=sb.set)


boxen = Tk()
boxen.title("OpenAnthroStat")
f = Frame(boxen)
fTitle = Frame(boxen)
fTxt = Frame(boxen)
fTitle.pack()
fTxt.pack()
f.pack()

# Create the title
title = Label(fTitle, height=2, width=50, text="OpenAnthroStat — Freelist Analysis")
title.pack()

#create the scroll bar
sb = Scrollbar(fTxt)
sb.pack(side=RIGHT, fill=Y)

# create the text box
tex = Text(fTxt, height=25, width=100)
tex.pack(side=LEFT, fill=Y)

# join
sb.config(command=tex.yview)
tex.config(yscrollcommand=sb.set)

# Buttons
b1 = Button(f, text='Input file', command=inputChooser)
b2 = Button(f, text='Output file', command=outputChooser)
b3 = Button(f, text='Run', command=launcher)
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=3)

# Run
mainloop()