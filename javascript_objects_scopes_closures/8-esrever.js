#!/usr/bin/node

exports.esrever = function (list) {
  const array1 = [];
  for (const i of list) {
    array1.unshift(i);
  }
  return array1;
};
