#!/usr/bin/node

const args = process.argv;

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }
  n = parseInt(n);
  if (n <= 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(args[2]));
