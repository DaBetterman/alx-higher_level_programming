#!/usr/bin/node

const argv = process.argv;
let num = 0;

if (argv.length < 3) {
  console.log('Not a number');
} else {
  num = parseInt(argv[2]);
  if (!isNaN(num) && Number.isInteger(num)) {
    console.log(num);
  } else {
    console.log('Not a number');
  }
}
