#!/usr/bin/node

const dict = require('./101-data').dict;

const sortedDict = {};
Object.entries(dict).forEach(([k, v]) => {
  sortedDict[v] ? sortedDict[v].push(k) : sortedDict[v] = [k];
});

console.log(sortedDict);
