import keylogger

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
				self.voiceOutput('You have selected: ' + selectedItem + '. Is it correct?')
				
				isCorrect = keylogger.getkey()
				
				if isCorrect == 'y':
					return selectedItem
			else: 
				return False
		
	def voiceOutput(self, out):
		""" Pronounce given output """
		print out