#!/usr/bin/node
const arg = process.argv;

const fs = require('fs');

fs.writeFile(arg[2], arg[3], err => {
  if (err) {
    console.error(err);
  }
});
