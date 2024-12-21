#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  for (let step = 0; step < list.length; step++) {
    if (list[step] === searchElement) {
      occurences++;
    }
  }
  return occurences;
};
