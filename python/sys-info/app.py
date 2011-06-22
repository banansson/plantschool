import subprocess

def isAlive(address):
  cmd = ['ping', '-c 1', '-n', address]
  proc = subprocess.Popen(cmd, stdout=PIPE)
  return proc

# prefered -- need to readup on how to use callbacks
def call(cmd, callback, errCallback):
  proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  retcode = proc.wait()
  if (retcode == 0):
    callback(proc.stdout.read())
  else:
    errCallback(proc.stderr.read())
  return retcode

def execute(cmd):
  proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  retcode = proc.wait()
  if retcode == 0:
    output = proc.stdout.read()
    if output == '':
      output = proc.stderr.read()
  else:
    output = proc.stderr.read()
  if output == '':
    return (retcode, '<no output on stdout>')
  return (retcode, output.strip())

def versionOf(app, part=0):
  cmd = [app, '--version']
  (returncode, output) = execute(cmd)
  if part == 0:
    return output
  return output.split()[part - 1]

def uptime():
  cmd = ['uptime']
  (returncode, output) = execute(cmd)
  return output.split()[0]

def systemName():
  cmd = ['uname', '--nodename']
  (returncode, output) = execute(cmd);
  return output

def hardwareName():
  cmd = ['uname', '--machine']
  (returncode, output) = execute(cmd);
  return output


def kernelVersion():
  cmd = ['uname', '-r']
  (returncode, output) = execute(cmd);
  return output

def gitVersion():
  return versionOf('git', 3)

def pythonVersion():
  return versionOf('python', 2)

def bashVersion():
  return versionOf('bash', 4)

if __name__ == '__main__':
  print '-- system --'
  print 'name   : %s' % systemName()
  print 'harware: %s' % hardwareName()
  print 'kernel : %s' % kernelVersion()
  print 'uptime : %s' % uptime()
  print '-- software --'
  print 'python : %s' % pythonVersion()
  print 'git    : %s' % gitVersion()
  print 'bash   : %s' % bashVersion()

