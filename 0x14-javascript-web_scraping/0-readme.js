#!/usr/bin/node
const arg = process.argv;

const fs = require('fs');

fs.readFile(arg[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
