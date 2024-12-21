#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0 && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let step = 0; step < this.height; step++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }

  double () {
    this.height = 2 * this.height;
    this.width = 2 * this.width;
  }
}

module.exports = Rectangle;
