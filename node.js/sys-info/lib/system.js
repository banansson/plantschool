/**
 * Read system data using uname
 *   What              Switch
 *  ---------------------------------------------------------------------------
 *   all               -a, --all                all information
 *   kernelName        -s, --kernel-name        kernel name 
 *   nodeName          -n, --nodename           network node hostname
 *   kernelRelease     -r, --kernel-release     kernel release
 *   kernelVersion     -v, --kernel-version     kernel version
 *   machineName       -m, --machine            machine hardware name
 *   processor         -p, --processor          processor type or "unknown"
 *   hardwarePlatform  -i, --hardware-platform  hardware platform or "unknown"
 *   operatingSystem   -o, --operating-system   operating system
 *
 **/

var sys   = require('sys');
var async = require('async');
var exec  = require('child_process').exec;

var sysinfo = module.exports;

sysinfo.kernelNameOne = function(callback) {
  var cmd = exec('uname -s', function(error, stdout, stderr) {
    callback(stdout);
  });
}

sysinfo.kernelName = function(callback) {
  var cmd = exec('uname -s', function(error, stdout, stderr) {
    callback(stdout);
  });
}

sysinfo.nodeName = function(callback) {
  var cmd = exec('uname -n', function(error, stdout, stderr) {
    callback(stdout);
  });
}

sysinfo.getAllSync = function(resultCallback) {
  async.parallel({
    kernelName: function(callback) {
      var cmd = exec('uname -s', function(error, stdout, stderr) {
        callback(null, stdout);
      });
    },
    nodeName: function(callback) {
      var cmd = exec('uname -n', function(error, stdout, stderr) {
        callback(null, stdout);
      });
    }
  },
  function(err, results) {
    resultCallback(results);
  });
}
