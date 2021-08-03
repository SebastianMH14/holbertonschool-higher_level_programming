#!/usr/bin/node
const arg = process.argv.slice(2);

if ((arg.length) < 2) {
  console.log(0);
} else {
  arg.sort((x, j) => x - j);
  console.log(arg[arg.length - 2]);
}
