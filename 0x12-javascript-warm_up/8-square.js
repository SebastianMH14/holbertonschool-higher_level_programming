#!/usr/bin/node
const arg = process.argv;

const x = parseInt(arg[2]);

if (x) {
  for (let i = 0; i < x; i++) {
    let square = 'X';
    for (let i = 1; i < x; i++) {
      square = square + 'X';
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
