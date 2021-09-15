#!/usr/bin/node
const request = require('request');
const arg = process.argv;

request.get({ url: arg[2], json: true },
  function (error, a, body) {
    if (error) {
      console.error(error);
    }
    const complete = {};
    for (const user of body) {
      if (user.completed) {
        if (complete[user.userId]) {
          complete[user.userId]++;
        } else {
          complete[user.userId] = 1;
        }
      }
    }
    console.log(complete);
  });
