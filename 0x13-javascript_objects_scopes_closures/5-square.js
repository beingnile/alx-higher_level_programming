#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size);
    if (isNaN(size) || size <= 0) {
      return this;
    }
    this.width = size;
    this.height = size;
  }
}

module.exports = Square;
