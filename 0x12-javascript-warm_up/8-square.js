#!/usr/bin/node

const argv = parseInt(process.argv[2]);
let i = 0;
let j = 0;

if (!isNaN(argv)) {
  for (i = 0; argv > i; i++) {
    for (j = 0; argv > j; j++) {
      process.stdout.write('X');
    } console.log('');
  }
} else {
  console.log('Missing size');
}
