**Note: The version found in this repository is in active development and is unstable. Please download the latest version, [Brisbane](https://github.com/Guerillero/OpenAnthroStat/releases/tag/Brisbane__v0.2.0-beta), instead.**

# OpenAnthroStat
A free Freelist analysis program in the early stages of development written in python 2.X. The goal is to create a fully 
functional platform for the analysis of freelists and pile sorts under a free licence. Currently, it can only analyze freelist 
data and has a very simple GUI written with `Tkinter`.

##Use
As long as everything in this package is in the same folder, general users shouldn't need to do anything more than 
double clicking on `OpenAnthroStat.py`. 

##Salience
OpenAnthroStat calculates Smith's S and Sutrop's S (Smith & Borgatti 1998; Sutrop 2001). Since they are not always the 
same, an average is taken and is displayed as `Aggregate S`.

####Functions
Stand alone functions to calculate both Smith's S and Sutrop's S can be found in `salience.py`.

##Troubleshoting
OpenAnthroStat is not compatible with python 3.0 or higher. While it is possible to force compatibility, doing this creates
comma separated files that are not easily imported into spreadsheet programs.

If you have found a bug, please submit it to the bug tracker here on GitHub. I will try to fix it as quick as I can.

Any other questions [can be sent to me](http://guerillero.net/contact).

##Change log
* [Adelaide](https://github.com/Guerillero/OpenAnthroStat/releases/tag/Adelaide__v0.1.0-alpha) - 20 May, 2015
* [Brisbane](https://github.com/Guerillero/OpenAnthroStat/releases/tag/Brisbane__v0.2.0-beta) - 21 May, 2015 - Bug fixes, adding a GUI, making the program self contained
* Canberra - October, 2015 (expected)
 
##Citations
Smith, J J & Borgatti, S. P. 1998. Salience Counts—And So Does Accuracy: Correcting and Updating a Measure for Free-List-Item Salience. *Journal of Linguistic Anthropology.* 7(2):208-209.

Sutrop, U. 2001. List task and a cognitive salience index. *Field Methods*. 13:263-276.
