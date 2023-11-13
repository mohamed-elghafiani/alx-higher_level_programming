#!/usr/bin/node

const args = process.argv;

function fact (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return n * fact(n - 1);
}

console.log(fact(Number(args[2])));
