#!/usr/bin/env node

var sysinfo = require('./lib/system.js');
var sys = require('sys');
var fs = require('fs');
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

app.get('/styles/:file', function(req, res) {
  fs.readFile(__dirname + '/styles/' + req.params.file, function(err, data) {
    res.writeHead(200, {'Content-Type':'text/css'});
    res.write(data);
    res.end();
  });
});

app.listen(port);
console.log('Server listening at port ' + port);

