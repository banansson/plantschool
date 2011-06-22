##
#  Photo backup script
#
#  By: Jan Olofsson <banansson@gmail.com>
#
##

import os

def sourceDir():
  return '~/Temp/Photos'

if __name__ == '__main__':
  source = os.path.expanduser(sourceDir());

  print 'Start...'
  print 'Source: ' + source

  # Set the stage
  os.chdir(source)

  # Build the file list
  sourceFiles = []
  for root, dirs, files in os.walk(source):
    for name in files:
      file = os.path.join(root, name)
      sourceFiles.append(file)

  # Investigate result
  for filePath in sourceFiles:
    print filePath

  print '...end'

