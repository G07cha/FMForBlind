import os
import shutil

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
		folders = []
		
		""" Filtering hidden files """
		for item in os.listdir(self.currentDir):
			if not item.startswith('.'):
				folders.append(item)
		
		return folders
	
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
	
	def removeItem(self, itemName):
		os.remove(filename)
		
	def copy(self, src, dst=False):
		if not dst:
			dst = self.currentDir
			
		shutil.copy(src, dst)
		self.output('Copied from ' + src + ' to ' + dst)
	
	def move(self, src, dst=False):
		if not dst:
			dst = self.currentDir
			
		shutil.move(src, dst)
		self.output('Moved from ' + src + ' to ' + dst)
		
	def getInfo(self, filename):
		self.output(os.stat(filename))
	
	""" Functions for managing output """
	def setOutput(self, output):
		self.output = output
	
	def getOutput(self):
		return self.output
	
	def unsetOutput(self):
		self.output = defaultOutput
		
def defaultOutput(out):
	return out