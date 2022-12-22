#!/usr/bin/node

const argv = require('process').argv;
const request = require('request');
const fs = require('fs');

request.get(argv[2], (error, response, body) => {
  if (error) {
    throw error;
  }
  fs.writeFile(argv[3], body, 'utf-8');
});
