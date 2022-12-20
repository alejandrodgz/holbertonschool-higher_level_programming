#!/usr/bin/node

require('process');

function convertNum (arr) {
  const array1 = [];
  for (const i of arr) {
    if (Number(i)) {
      array1.push(Number(i));
    }
  }
  console.log(array1);
  return array1;
}

function secGreat (arr) {
  let a = 0;
  let b = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > a) {
      a = arr[i];
    }
  }

  for (let j = 0; j < arr.length; j++) {
    if (arr[j] > b && arr[j] < a) {
      b = arr[j];
    }
  }
  return b;
}
if (process.argv.length < 3) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  const arrayArgv = convertNum(process.argv);
  console.log(secGreat(arrayArgv));
}
