#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let j;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      j++;
    }
  }
  return (j);
};
