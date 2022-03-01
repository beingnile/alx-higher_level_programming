#!/usr/bin/node

// Class 'Rectangle' defines a Rectangle
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let hgt = 0; hgt < this.height; hgt++) {
      let line = '';
      for (let wid = 0; wid < this.width; wid++) {
        line += 'X';
      }
      console.log(line);
    }
  }
};
