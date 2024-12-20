#!/usr/bin/node

const args = process.argv;

if (isNaN(args[2]) || isNaN(args[3])) {
  console.log(0);
} else {
  let largest = Math.max(args[2], args[3]);
  let secondLargest = Math.min(args[2], args[3]);

  if (args.length > 4) {
    for (let i = 4; i < args.length; i++) {
      const current = Number(args[i]);
      if (current > largest) {
        secondLargest = largest;
        largest = current;
      } else if (current > secondLargest && current < largest) {
        secondLargest = current;
      }
    }
  }
  console.log(secondLargest);
}
