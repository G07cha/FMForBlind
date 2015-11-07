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
        v.voiceOutput('Select folder to navigate')
        folder = v.selectFrom(['..'] + fs.scanDir())
        if folder:
            fs.navigate(folder)
    elif key == 'm':
        """ mkdir """

        while True:
            v.voiceOutput("Enter name for new folder")
            folder = raw_input("Enter name for folder: ")
            if folder:
                if v.prompt(folder):
                    fs.mkdir(folder)
		    break
            else:
                break
    elif key == 'o':
        """ xdg-open or touch """

        while True:
            v.voiceOutput("Enter item name to open")
            filename = raw_input("Enter filename: ")
            if filename:
                if v.prompt(filename):
                    if fs.isItemExists(filename):
                        fs.openFile(filename)
                    else:
                        fs.createFile(filename)
                        fs.openFile(filename)
		break
            else:
                break
    elif key == 'd':
        """ rm """
        while True:
            v.voiceOutput("Select item to remove")
            filename = v.selectFrom(fs.scanDir())
            if filename:
                if v.prompt(filename):
                    fs.removeItem(filename)
		    break
            else:
                break
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
        item = v.selectFrom(fs.scanDir())
        if item:
            fs.getInfo(item)

    elif key == 'f':
        """ find . -name """
        while True:
            v.voiceOutput("Enter name to find")
            filename = raw_input("Enter itemname: ")
            if filename:
                if v.prompt(filename):
                    fs.findItem(filename)
		    break
            else:
                break
    else:
        print "Invalid output\a"
