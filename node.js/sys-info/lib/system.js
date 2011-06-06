var sys = require('sys');
var sysinfo = module.exports;
var exec = require('child_process').exec;
var spawn = require('child_process').spawn;

sysinfo.getName = function(callback) {
  var cmd = exec('uname -n', function(error, stdout, stderr) {
    callback(stdout);
  });
}

sysinfo.getAll = function(callback) {
  var cmd = exec('uname -a', function(error, stdout, stderr) {
    callback(stdout);
  });
}

