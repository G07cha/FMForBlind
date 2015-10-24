import os

class FS:
	def __init__(self, output=False):
		self.currentDir = os.environ['HOME'] + '/'
		os.chdir(self.currentDir)
		if output:
			self.output = output
		else:
			self.output = defaultOutput
		
	def navigate(self, folder):
		if folder == '..':
			""" Searching for second '/' symbol from end and removing everything after it """
			self.currentDir = self.currentDir[0:self.currentDir.rfind('/', 0, len(self.currentDir) - 1) + 1]
		else:
			self.currentDir = self.currentDir + folder + '/'
		
		self.output('Now you are in ' + self.currentDir)
		os.chdir(self.currentDir)
	
	def scanDir(self):
		return os.listdir(self.currentDir)
	
	def mkdir(self, name):
		os.mkdir(name)
	
	def getDir(self):
		self.output(self.currentDir)
	
	def isItemExists(self, item):
		return item in scanDir()
	
	def openFile(self, filename):
		os.system("xdg-open " + filename)
	
	def createFile(self, filename):
		open(filename, "w+").close()
	
	def editFile(self, filename):
		f = open(filename, "w")
		return f
	
	def removeItem(self, itemName):
		os.remove(filename)
	
	""" Functions for managing output """
	def setOutput(self, output):
		self.output = output
	
	def getOutput(self):
		return self.output
	
	def unsetOutput(self):
		self.output = defaultOutput
		
def defaultOutput(out):
	return out