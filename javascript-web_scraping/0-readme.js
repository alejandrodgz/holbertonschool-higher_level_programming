#!/usr/bin/node

const fs = require('fs');
const argv = require('process').argv;

fs.readFile(argv[2], 'utf-8', (error, data) => {
  if (error) {
    throw error;
  } else {
    console.log(data);
  }
});
