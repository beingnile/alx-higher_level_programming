#!/usr/bin/node

const request = require('request');
const episode = process.argv[2];
const films = 'https://swapi-api.hbtn.io/api/films/';

request(films + episode, function (error, response, body) {
  if (error) {
    throw error;
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
