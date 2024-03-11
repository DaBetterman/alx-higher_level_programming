#!/usr/bin/node

const argv = process.argv;
let i = 2;
let bool = false;

for (i = 2; argv[i] !== undefined; i++) {
  console.log(argv[i]);
  bool = true;
}
if (!bool) {
  console.log('No arguments');
}
