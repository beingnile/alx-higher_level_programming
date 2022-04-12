#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  console.error(error);
  console.log('code: ', response && response.statusCode);
});
