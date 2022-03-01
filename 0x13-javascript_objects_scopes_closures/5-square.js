#!/usr/bin/node

// Class 'Square' defines a square
// and inherits from class 'Rectangle'
module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
