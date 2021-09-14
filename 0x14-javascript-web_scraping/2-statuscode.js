#!/usr/bin/node
const request = require('request');
const arg = process.argv;

request
  .get(arg[2])
  .on('response', function (response) {
    console.log('code:', response.statusCode); // 200
  });
