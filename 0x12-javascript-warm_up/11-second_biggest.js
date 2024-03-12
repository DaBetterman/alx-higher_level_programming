#!/usr/bin/node

const argv = process.argv.slice(2).map(Number);

if (argv.length <= 1) {
  console.log(0);
} else {
  const sortedArgv = argv.sort((a, b) => b - a);
  console.log(sortedArgv[1]);
}
