#!/usr/bin/node

const request = require('request');
const argv = require('process').argv;

const url = 'https://swapi-api.hbtn.io/api/films/' + String(argv[2]);
request.get(url, (error, response, body) => {
  console.log(JSON.parse(body).title);
});
