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
        folder = v.selectFrom(fs.scanDir())
        if folder:
            fs.navigate(folder)
    elif key == 'm':
        """ mkdir """

        while True:
            folder = raw_input("Enter name for folder: ")
            if folder:
                if v.promt(folder):
                    fs.mkdir(folder)
            else:
                break
    elif key == 'o':
        """ xdg-open or touch """

        while True:
            filename = raw_input("Enter filename: ")
            if filename:
                if v.promt(filename):
                    if fs.isItemExists(filename):
                        fs.openFile(filename)
                    else:
                        fs.createFile(filename)
                        fs.openFile(filename)
            else:
                break
    elif key == 'd':
        """ rm """
        filename = v.selectFrom(fs.scanDir())
        if filename:
            fs.removeItem(filename)
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
            filename = raw_input("Enter itemname: ")
            if filename:
                if v.promt(filename):
                    fs.findItem(filename)
            else:
                break;
    else:
        print "Invalid output\a"
