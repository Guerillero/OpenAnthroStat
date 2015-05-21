# OpenAnthroStat
A free Freelist analysis program in the early stages of development written in python 2.X. The goal is to create a fully 
functional platform for the analysis of freelists and pile sorts under a free licence. Currently, it can only anylize freelist 
data and has a very simple GUI written with `Tkinter`.

##Use
As long as everything in this package is in the same directory, general users shouldn't need to do anything more than running `OpenAnthroStat.py`. 

##Salience
OpenAnthroStat calculates Smith's S and Sutrop's S (Smith & Borgatti 1998; Sutrop 2001). Since they are not always the 
same, an average is taken and is displayed as `Aggregate S`. 

###Functions
Stand alone functions to calculate both Smith's S and Sutrop's S can be found in `salience.py`.
 
##Citations
Smith, J J & Borgatti, S. P. 1998. Salience Counts—And So Does Accuracy: Correcting and Updating a Measure for Free-List-Item Salience. *Journal of Linguistic Anthropology.* 7(2):208-209.

Sutrop, U. 2001. List task and a cognitive salience index. *Field Methods*. 13:263-276.