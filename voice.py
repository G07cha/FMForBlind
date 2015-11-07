import keylogger
import pyttsx


engine = pyttsx.init()
def onEnd(name, completed):
    if completed:
        engine.endLoop()
        
engine.connect('finished-utterance', onEnd)
engine.setProperty('voice', 'english')
engine.setProperty('rate', 150)

class Voice:
    def __init__(self, options=False):
        if options:
            self.options = options

    """ Pronounce list with numbers to select and then asked for selection """

    def selectFrom(self, array):
        while True:
            index = 0
            for item in array:
                index += 1
                self.voiceOutput(str(index) + ' ' + item)

            selectedIndex = raw_input('Enter item number: ')

            if selectedIndex:
                selectedItem = array[int(selectedIndex) - 1]
                if self.prompt(selectedItem):
                    return selectedItem
            else:
                return False

    def prompt(self, selectedOption):
        self.voiceOutput('You have selected: ' + selectedOption + '. Is it correct?')

        isCorrect = keylogger.getkey()
        print isCorrect
        if isCorrect == 'y':
            return True
        else:
            return False

    def voiceOutput(self, out):
        """ Pronounce given output """
        print out
        engine.say(out)
        engine.startLoop()
        """ Temporary fix for jammed every second command """
        engine.say(' ')
        engine.startLoop()
