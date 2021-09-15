#!/usr/bin/node
const arg = process.argv;
const request = require('request');

request.get(arg[2], function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  let i = 0;
  for (const e of JSON.parse(body).results) {
    for (const a of e.characters) {
      if (a.endsWith('/18/')) {
        i++;
      }
    }
  }
  console.log(i);
});
