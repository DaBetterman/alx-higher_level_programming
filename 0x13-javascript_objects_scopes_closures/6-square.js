#!/usr/bin/node

const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (C) {
    let i = 0;
    let j = 0;
    let temp = '';

    if (C === undefined) {
      temp = 'X';
    } else {
      temp = 'C';
    }
    for (i = 0; i < this.width; i++) {
      for (j = 0; j < this.height; j++) {
        process.stdout.write(temp);
      }
      console.log();
    }
  }
}
module.exports = Square;
