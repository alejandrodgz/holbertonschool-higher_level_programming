#!/usr/bin/node

require('process');

if (Number(process.argv[2])) {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('X'.repeat(Number(process.argv[2])));
  }
} else {
  console.log('Missing size');
}
