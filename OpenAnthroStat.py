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


def about():
    output = "OpenAnthroStat Version Brisbane (0.2.0) -- Released on 21 May, 2015.\n" \
             "https://github.com/Guerillero/OpenAnthroStat \n\nAbout Salience:\nOpenAnthroStat calculates " \
             "Smith's S and Sutrop's S (Smith & Borgatti 1998; Sutrop 2001).\n" \
             "Since they are not always the same, an average is taken and is displayed as Aggregate S." \
             "\n\n\nuLicensing Information: \n\n" + MIT

    #update the text
    tex.insert(END, output)
    sb.config(command=tex.yview)
    tex.config(yscrollcommand=sb.set)

boxen = Tk()
boxen.title("OpenAnthroStat")
fbutton = Frame(boxen, padx=10, pady=20)
fTitle = Frame(boxen)
fTxt = Frame(boxen)
fRadioButton = Frame(boxen, padx=2, pady=5)

# pack
fTitle.pack()
fTxt.pack()
fRadioButton.pack()
fbutton.pack()

# Create the title
title = Label(fTitle, height=2, width=50, text="OpenAnthroStat — FreeList Analysis", font="default 20 bold italic")
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
b1 = Button(fbutton, text='Input file', command=inputChooser, padx=2, pady=2)
b2 = Button(fbutton, text='Output file', command=outputChooser, padx=2, pady=2)
b3 = Button(fbutton, text='Run', command=launcher, padx=2, pady=2)
b4 = Button(fbutton, text='About', command=about, padx=2, pady=2)
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=0, column=3)

# Radio Buttons. For future use.
v = StringVar()
#rbL = Label(fRadioButton, height=2, width=30, text="Data Type (Non-Operational)")
rb1 = Radiobutton(fRadioButton, text="FreeList", variable=v, value=1)
#rbL.grid(row=0, column=0)
rb1.grid(row=1, column=0)

# Run
mainloop()