#!/usr/bin/node

const argv = parseInt(process.argv[2]);
let i = 0;

if (!isNaN(argv) && argv > 0) {
  while (argv !== i) {
    console.log('C is fun');
    i++;
  }
} else if (isNaN(argv)) {
  console.log('Missing number of occurrences');
}
