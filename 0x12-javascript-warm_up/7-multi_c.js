#!/usr/bin/node
const arg = process.argv;

const x = parseInt(arg[2]);

if (x) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
