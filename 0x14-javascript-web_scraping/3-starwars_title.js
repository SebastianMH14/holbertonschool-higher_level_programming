#!/usr/bin/node
const request = require('request');
const arg = process.argv;

request.get({ url: 'https://swapi-api.hbtn.io/api/films/' + arg[2], json: true },
  function (error, a, body) {
    if (error) {
      console.error(error);
    }
    console.log(body.title);
  });
