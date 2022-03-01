#!/usr/bin/node

// Class 'Square' defines a square
// and inherits from class 'Rectangle'
module.exports = class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let hgt = 0; hgt < this.height; hgt++) {
        let line = '';
        for (let wid = 0; wid < this.width; wid++) {
          line += c;
        }
        console.log(line);
      }
    }
  }
};
