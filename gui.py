import Tkinter as tk
import tkFileDialog as tkFD

importFile = ""
outputFile = ""

def callback(numb):
    if numb == 1:
        config.importFile = tkFD.askopenfilename()
    else:
        config.outputFile = tkFD.askopenfilename()


boxen = tk.Tk()
tk.Button(text='Input file', command=callback(1).pack())
tk.Button(text='Output file', command=callback(2).pack())
boxen.mainloop()
