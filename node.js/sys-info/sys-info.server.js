#!/usr/bin/env node

var sysinfo = require('./lib/system.js');
var sys = require('sys');
require('ejs');
var express = require('express');
var app = express.createServer();
var port = 60606;

app.set('view engine', 'ejs');
app.set('view options', { layout: false });

app.get('/', function(req, res) {
  console.log(req.method + ' ' +
    req.url +
    ' from ' + req.client.remoteAddress + ':' + req.client.remotePort + 
    ' [' + req.headers['user-agent'] + ']');
    sysinfo.getAllSync(function(model) {
      console.log(sys.inspect(model));
      res.render('main', {
        locals: model
      });
    });
});

app.listen(port);
console.log('Server listening at port ' + port);

