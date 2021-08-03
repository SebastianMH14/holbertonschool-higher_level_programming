#!/usr/bin/node
const arg = process.argv;

function add (a, b) {
  return (a + b);
}
console.log(add(parseInt(arg[2]), parseInt(arg[3])));
