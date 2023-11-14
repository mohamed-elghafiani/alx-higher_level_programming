#!/usr/bin/node

const Square_ = require('./5-square');

class Square extends Square_ {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
