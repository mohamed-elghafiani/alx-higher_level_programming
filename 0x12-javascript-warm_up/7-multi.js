#!/usr/bin/node

const args = process.argv;
const num = Number(args[2]);
if (!num) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < num; i++) {
  console.log('C is fun');
}
