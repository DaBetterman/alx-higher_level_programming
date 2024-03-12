#!/usr/bin/node

class Rectangle {
  constructor (h, w) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      return 'Rectangle {}';
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let j = 0;

    for (i = 0; this.width > i; i++) {
      for (j = 0; this.height > j; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
