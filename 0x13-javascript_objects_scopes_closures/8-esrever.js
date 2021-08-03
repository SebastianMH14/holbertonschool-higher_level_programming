#!/usr/bin/node

exports.esrever = function (list) {
  const n = [];
  const len = list.length - 1;
  for (let i = len; i >= 0; i--) {
    n.push(list[i]);
  }
  return (n);
};
