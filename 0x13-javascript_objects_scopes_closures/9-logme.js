#!/usr/bin/node

let argc = 0;
exports.logMe = function (item) {
  argc++;
  console.log(`${argc}: ${item}`);
};
