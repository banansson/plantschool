#!/usr/bin/env node
/**
 * A well known example of a node.js server
 **/

var http = require('http');

var server = http.createServer(function(req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello user!');
});

server.listen(8080);
