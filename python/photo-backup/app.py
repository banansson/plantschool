##
#  Photo backup script
#
#  By: Jan Olofsson <banansson@gmail.com>
#
##

import os
import sys

def usage(argv):
  print "Usage: %s [dir]" % argv[0]

def main(argv):
  try:
    requested = argv[1]
  except:
    usage(argv)
    sys.exit(2)

  source = os.path.expanduser(requested);

  print 'Source: ' + source

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
  totalSize = 0
  for filePath in sourceFiles:
    info = os.stat(filePath)
    size = info.st_size
    totalSize += size
    megabytes = float(size) / (1024 * 1024)
    print '%s %.1fMB' % (filePath, megabytes)

  print '%d files %.1fMB (%d bytes)' % (fileCount, totalSize / (1024 * 1024), totalSize)

if __name__ == '__main__':
  main(sys.argv)

