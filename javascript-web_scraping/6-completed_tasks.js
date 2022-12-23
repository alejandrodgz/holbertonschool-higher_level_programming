#!/usr/bin/node

const request = require('request');
const argv = require('process').argv;

const url = argv[2];
request.get(url, (error, response, body) => {
  if (error) {
    throw error;
  }
  const data = JSON.parse(body);
  const obj = {};
  for (const elem of data) {
    if (elem.completed) {
      obj[String(elem.userId)] = obj[String(elem.userId)] + 1 || 1;
    }
  }
  /* if (elem.completed) {
      if (!(String(elem.userId) in obj)) {
        obj[String(elem.userId)] = 1;
      } else {
        obj[String(elem.userId)] += 1;
      }
    }
  } */
  console.log(obj);
});
