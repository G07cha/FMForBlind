import os, fnmatch, shutil, datetime

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

    def scanDir(self, foldersOnly=False):
        folders = []

        """ Filter hidden files """
        for item in os.listdir(self.currentDir):
            if not item.startswith('.'):
				if foldersOnly == False or '.' not in item:
				     folders.append(item)

        return folders

    def mkdir(self, name):
        os.mkdir(name)

    def getDir(self):
        self.output(self.currentDir)

    def isItemExists(self, item):
        return item in self.scanDir()

    def openFile(self, filename):
        os.system("xdg-open " + filename)

    def createFile(self, filename):
        open(filename, "w+").close()

    def removeItem(self, filename):
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
        info = os.stat(filename)
        self.output('Size ' + str(info.st_size) +
                    ' bytes, created at ' + parseTimestamp(info.st_ctime) +
                    ', last modified at ' + parseTimestamp(info.st_mtime))

    def findItem(self, itemname):
        result = []

        for root, dirs, files in os.walk(self.currentDir):
            for name in files:
                if fnmatch.fnmatch(name, itemname):
                    result.append(os.path.join(root, name))

        self.output(result)

    """ Functions for managing output """

    def setOutput(self, output):
        self.output = output

    def getOutput(self):
        return self.output

    def unsetOutput(self):
        self.output = defaultOutput


def defaultOutput(out):
    return out

def parseTimestamp(timestamp):
    return str(datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S %d-%m-%Y'))