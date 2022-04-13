#!/usr/bin/node

const request = require('request');
const myurl = process.argv[2];

request(myurl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ', response.statusCode);
  }
});
