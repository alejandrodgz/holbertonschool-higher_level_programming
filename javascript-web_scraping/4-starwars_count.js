#!/usr/bin/node

const request = require('request');
const argv = require('process').argv;

const url = argv[2];
const id = 18;
request.get(url, (error, response, body) => {
  if (error) {
    throw error;
  }
  let a = 0;
  for (const i of JSON.parse(body).results) {
    for (const j of i.characters) {
      if (j.includes(String(id))) {
        a++;
      }
    }
  }
  console.log(a);
});
