#!/usr/bin/node

const fs = require('fs');

const argv = process.argv;

const fileA = argv[2];
const fileB = argv[3];
const fileC = argv[4];

const contentA = fs.readFileSync(fileA);
const contentB = fs.readFileSync(fileB);

fs.writeFileSync(fileC, contentA + contentB);
