from os import *

class FS:
	def __init__(self, output=False):
		self.currentDir = environ['HOME'] + '/'
		if output:
			self.output = output
		else:
			self.output = defaultOutput
		
	def navigate(self, folder):
		if folder == '..':
			""" Searching for second '/' symbol from end and removing everything after it """
			self.currentDir = self.currentDir[0:self.currentDir.rfind('/', 0, len(self.currentDir) - 1) + 1]
		else:
			""" Checking if folder exists """
#			if folder in self.scanDir():
			self.currentDir = self.currentDir + folder + '/'
#			else:
#				self.output('This folder doesn\'t exists')
		self.output('Now you are in ' + self.currentDir)
	
	def scanDir(self):
		self.output(listdir(self.currentDir))
	
	def mkdir(self, name):
		mkdir(self.currentDir + name)
	
	def getDir(self):
		self.output(self.currentDir)
	
	def setOutput(self, output):
		self.output = output
	
	def getOutput(self):
		return self.output
	
	def unsetOutput(self):
		self.output = defaultOutput
		
def defaultOutput(out):
	return out