#!/usr/bin/node
const arg = process.argv;
const n = parseInt(arg[2]);

function fact (i) {
  if (isNaN(i)) {
    return (1);
  } else if (i === 0) {
    return (1);
  } else {
    return (i * fact(i - 1));
  }
}

console.log(fact(n));
