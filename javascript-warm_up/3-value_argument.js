#!/usr/bin/node

require('process');

if (process.argv.length >= 2) {
  console.log(process.argv[2]);
} else if (process.argv.length < 2) {
  console.log('No argument');
}
