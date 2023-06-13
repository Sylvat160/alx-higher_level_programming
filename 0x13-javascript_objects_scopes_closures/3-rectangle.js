#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) return ({});
    this.width = w;
    this.height = h;
  }

  print () {
    let i = 0;
    let j = 0;
    let str = '';
    for (; i < this.height; i++) {
      for (; j < this.width; j++) {
        str += 'X';
      }
      console.log(str);
      str = '';
      j = 0;
    }
  }
}

module.exports = Rectangle;
