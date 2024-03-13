#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  let i = 0;
  const count = list.length;

  for (i = 0; list[i] !== undefined; i++) {
    newList[count - i - 1] = list[i];
  }
  return newList;
};
