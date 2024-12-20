#!/usr/bin/node

const args = process.argv;

if (isNaN(args[2])) {
  console.log('Missing number of occurrences');
} else if (parseInt(args[2]) > 0) {
  let i = 0;
  while (i !== parseInt(args[2])) {
    console.log('C is fun');
    i++;
  }
}
