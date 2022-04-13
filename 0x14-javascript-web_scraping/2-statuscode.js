#!/usr/bin/node

const request = require('request');
const myurl = process.argv[2];

request(myurl, function (error, response, body) {
  if (error) throw error;
  console.log('code: ', response.statusCode);
});
