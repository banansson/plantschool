#!/usr/bin/env node

var ejs = require('ejs');
var express = require('express');
var app = express.createServer();

app.set('view engine', 'ejs');
app.get('/', function(req, res) {
  res.render('main', {
      layout: false,
      locals: { name: 'localhost' }
    });
});

app.listen(60606);

