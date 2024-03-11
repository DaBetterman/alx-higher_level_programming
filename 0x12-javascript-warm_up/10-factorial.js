#!/usr/bin/node

const argv = parseInt(process.argv[2]);

const result = factorial(argv);
console.log(result);

function factorial (n) {
  if (isNaN(n)) {
    return (1);
  } else if (n === 1) {
    return (1);
  }
  return n * factorial(n - 1);
}
