################################################################################
#Conway's Game of Life (Python 3.6 implementation)                             #
################################################################################
#(creative commons) Jon Patton May 11, 2017                                    #
################################################################################
#This is an implementation of Dr. John H. Conway's game of life in Python 3.   #
#It has some random generation elements to ensure that there are fewer steady  #
#states and dynamic sizing. The bones are also there if you want to let the    #
#user change the speed of generation.                                          #
#See https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for rules etc.      #
################################################################################

Uses a unicode character above 128, and the clear function for Unix/Linux.

These aspects may have to be changed to run on some systems. E.g., the block
character doesn’t display in Cloud9 IDE.ß