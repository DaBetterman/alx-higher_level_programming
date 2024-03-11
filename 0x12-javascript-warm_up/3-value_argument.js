#!/usr/bin/node

const [, , argv] = process.argv;

if (argv) {
  console.log(argv);
} else {
  console.log('No arguments');
}
