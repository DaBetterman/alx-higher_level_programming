#!/usr/bin/node

const process = require('process');
const argv = process.argv[2];

if (argv === undefined) {
  console.log('No arguments');
} else {
  console.log(argv);
}
