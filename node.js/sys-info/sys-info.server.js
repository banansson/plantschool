#!/usr/bin/env node

var sysinfo = require('./lib/system.js');
require('ejs');
var express = require('express');
var app = express.createServer();
var port = 60606;

app.set('view engine', 'ejs');
app.get('/', function(req, res) {
  sysinfo.getName(function(name) {
    res.render('main', {
      layout: false,
      locals: { name: name }
    });   
  });
});

app.listen(port);
console.log('Server listening at port ' + port);

