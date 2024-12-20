#!/usr/bin/node

const args = process.argv;

if (isNaN(args[2])) {
  console.log('Missing size');
} else if (parseInt(args[2]) > 0) {
  const size = parseInt(args[2]);

  for (let init = 0; init < size; init++) {
    console.log('x'.repeat(size));
  }
}
