#!/usr/bin/python

import voice
import keylogger
from fs import FS


""" Output for debugging """
def onScreenOutput(out):
	print out

""" Mounting output to file system """
fs = FS(onScreenOutput)

""" Main loop """
while True:
	key = keylogger.getkey()
	
	if key == 'l':
		""" ls """
		fs.scanDir()
	elif key == 'd':
		""" pwd """
		fs.getOutput()(fs.currentDir)
	elif key == 'n':
		""" cd """
		folder = raw_input("Enter folder: ")
		fs.navigate(folder)
	elif key == 'm':
		""" mkdir """
		folder = raw_input("Enter name for folder: ")
		fs.mkdir(folder)
	elif key == 'o':
		""" xdg-open or touch """
		filename = raw_input("Enter filename: ")
		if fs.isItemExists(filename):
			fs.openFile(filename)
		else:
			fs.createFile(filename)
			fs.editFile(filename)
	elif key == 'd':
		""" rm """
		filename = raw_input("Enter itemname: ")
		fs.removeItem()
	elif key == 'r':
		""" mv(rename) """
	elif key == 'c':
		""" copy """
	elif key == 'i':
		""" get properties """
	elif key == 'f':
		""" find . -name """
	else:
		print "Invalid output\a"