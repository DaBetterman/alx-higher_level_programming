#!/usr/bin/node

let i = 0;
exports.callMeMoby = function callMeMoby (x, theFunction) {
  for (i = 0; x > i; i++) {
    theFunction();
  }
};
