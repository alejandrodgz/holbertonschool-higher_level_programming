#!/usr/bin/node

const argv = require('process').argv;
const fs = require('fs');

fs.writeFile(argv[2], argv[3], 'utf-8', function (error) {
  if (error) {
    throw error;
  }
});
