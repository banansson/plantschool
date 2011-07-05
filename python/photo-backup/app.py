##
#  Photo backup script
#
#  By: Jan Olofsson <banansson@gmail.com>
#
##

import os
import sys

class Support:
  def __init__(self):
    self.kilobyte = 1024
    self.megabyte = self.kilobyte * 1024
    self.terabyte = self.megabyte * 1024
    self.petabyte = self.terabyte * 1024

  def weight(self, size):
    if (size < self.kilobyte):
      return (size, ' bytes')
    if (size < self.megabyte):
      return (size / self.kilobyte, 'kB')
    if (size < self.terabyte):
      return (size / self.megabyte, "MB")
    if (size < self.petabyte):
      return (size / self.terabyte, "GB")

class App:
  def __init__(self, support, arguments):
    self.arguments = arguments
    self.support = support

  def usage(self):
    print "Usage: %s [dir]" % self.arguments[0]

  def run(self):
    requested = self.arguments[1]

    # Validate source
    source = os.path.expanduser(requested);
    if not os.path.exists(source):
      print 'No such location: ' + source
      return 2

    # Set the stage
    os.chdir(source)

    # Build the file list
    sourceFiles = []
    for root, dirs, files in os.walk(source):
      for name in files:
        current = os.path.join(root, name)
        sourceFiles.append(current)

    # Investigate result
    fileCount = len(sourceFiles)
    totalBytes = 0
    for filePath in sourceFiles:
      info = os.stat(filePath)
      size = info.st_size
      totalBytes += size
      weightedBytes, postfix = support.weight(size)

    totalSize, totalSizePostfix = support.weight(totalBytes)
    return (fileCount, totalSize, totalSizePostfix, totalBytes)

if __name__ == '__main__':
  support = Support()
  app = App(support, sys.argv)
  try:
    (fileCount, totalSize, totalSizePostfix, totalBytes) = app.run()
    print '%d files %.1f%s (%d bytes)' % (fileCount, totalSize, totalSizePostfix, totalBytes)
  except:
    app.usage()

