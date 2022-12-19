#!/usr/bin/node

require('process');

function factorial (a) {
  if (a <= 0) {
    return 1;
  } else if (a > 0) {
    return (a * factorial(a - 1));
  } else {
    return 1;
  }
}

const a = Number(process.argv[2]);
console.log(factorial(a));
