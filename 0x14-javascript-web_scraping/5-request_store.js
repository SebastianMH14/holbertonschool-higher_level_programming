#!/usr/bin/node
const arg = process.argv;
const request = require('request');
const fs = require('fs');

request.get({ url: arg[2] }, function (error, r, body) {
  if (error) {
    console.error(error);
  }
  fs.writeFile(arg[3], body, err => {
    if (err) {
      console.error(err);
    }
  });
});
