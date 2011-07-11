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

def weight(size):
  kilobyte = 1024
  megabyte = kilobyte * 1024
  terabyte = megabyte * 1024
  petabyte = terabyte * 1024

  if (size < kilobyte):
    return (size, ' bytes')
  if (size < megabyte):
    return (size / kilobyte, 'kB')
  if (size < terabyte):
    return (size / megabyte, "MB")
  if (size < petabyte):
    return (size / terabyte, "GB")

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
  totalBytes = 0
  for filePath in sourceFiles:
    info = os.stat(filePath)
    size = info.st_size
    totalBytes += size
    megabytes, postfix = weight(size)
    print '%s %.1f%s' % (filePath, megabytes, postfix)

  totalSize, totalSizePostfix = weight(totalBytes)
  print '%d files %.1f%s (%d bytes)' % (fileCount, totalSize, totalSizePostfix, totalBytes)

if __name__ == '__main__':
  main(sys.argv)

