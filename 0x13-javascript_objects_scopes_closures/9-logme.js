#!/usr/bin/node

let argc = -1;
exports.logMe = function (item) {
  ++argc;
  console.log(`${argc}: ${item}`);
};
