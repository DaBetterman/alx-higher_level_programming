#!/usr/bin/node

const argv = process.argv;
let result;

if (argv.length < 3) {
  console.log('NaN');
} else if (argv.length >= 3) {
  result = add(argv[2], argv[3]);
  console.log(result);
}

function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  return (a + b);
}
