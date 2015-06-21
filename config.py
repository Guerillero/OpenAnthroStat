###############################################################
#
#       This is the OpenAnthroStat config file 
#
#  To overide the defaults, go to the very bottom of the file
#  The text document to be imported goes in 'importFile'
#  The place where the resulting CSVs should go goes in 'outputFile'
#
###################################################################
import sys

# Linux, BSD, and Cygwin
if sys.platform.startswith('linux') or sys.platform.startswith('freebsd') or sys.platform.startswith('cygwin'):
    importFile = "\\tmp\\data.txt"
    outputFile = "\\tmp\\"

# Windows
elif sys.platform.stsartswith('win'):
    importFile = "C:\\AP\\data.txt"
    outputFile = "C:\\AP\\"

# Mac OSX
elif sys.platform.startdwith('darwin'):
    # I am using the BSD options for now
    importFile = "\\tmp\\data.txt"
    outputFile = "\\tmp\\"

else:
    # Does anyone even use OS2, RiscOS, or AethOS?
    # I don't know the file system so they live in the same directory
    importFile = "data.txt"
    outputFile = ""

# OVERIDE: Change the False to True
if False:
    importFile = "" # Data to import
    outputFile = "" # Output file


