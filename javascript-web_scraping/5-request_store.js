#!/usr/bin/node

const argv = require('process').argv;
const request = require('request');
const fs = require('fs');

request.get(argv[2]).pipe(fs.createWriteStream(argv[3]));
