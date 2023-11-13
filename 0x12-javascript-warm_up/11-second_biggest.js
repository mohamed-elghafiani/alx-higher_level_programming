#!/usr/bin/node

const args = process.argv;
if (args.length <= 3) {
  console.log(1);
} else {
  const nums = args.slice(2).map(el => Number(el));
  console.log(Math.max(...nums.filter(el => el !== Math.max(...nums))));
}
