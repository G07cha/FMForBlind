#!/usr/bin/python

from voice import Voice
import keylogger
from fs import FS


v = Voice()
""" Mounting output to file system """
fs = FS(v.voiceOutput)

selectedItem = ''
""" Main loop """
while True:
	key = keylogger.getkey()
	
	if key == 'l':
		""" ls """
		fs.getOutput()(fs.scanDir())
	elif key == 'p':
		""" pwd """
		fs.getOutput()(fs.currentDir)
	elif key == 'n':
		""" cd """
		folder = raw_input("Enter folder: ")
		if folder:
			fs.navigate(folder)
	elif key == 'm':
		""" mkdir """
		folder = raw_input("Enter name for folder: ")
		if folder:
			fs.mkdir(folder)
	elif key == 'o':
		""" xdg-open or touch """
		filename = raw_input("Enter filename: ")
		if filename:
			if fs.isItemExists(filename):
				fs.openFile(filename)
			else:
				fs.createFile(filename)
				fs.editFile(filename)
	elif key == 'd':
		""" rm """
		filename = raw_input("Enter itemname: ")
		if filename:
			fs.removeItem()
	elif key == 's':
		""" select """
		selection = v.selectFrom(fs.scanDir())
		if selection:
			selectedItem = fs.currentDir + selection
	elif key == 'x':
		""" move """
		if selectedItem:
			fs.move(selectedItem)
			selectedItem = ''
		else:
			v.voiceOutput("Please select item first")
	elif key == 'c':
		""" copy """
		if selectedItem:
			fs.copy(selectedItem)
			selectedItem = ''
		else:
			v.voiceOutput("Please select item first")
	elif key == 'i':
		""" get properties """
		
	elif key == 'f':
		""" find . -name """
	else:
		print "Invalid output\a"