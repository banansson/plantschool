var sys = require('sys');
var sysinfo = module.exports;
var exec = require('child_process').exec;

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

sysinfo.getEverything = function(callback) {
  var model = { };
  sysinfo.getName(function(data) {
    model.name = data;
    callback(model);
  });
}

