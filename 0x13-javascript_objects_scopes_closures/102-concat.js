const fs = require('fs');
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) {
    return console.error(err);
  }

  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) {
      return console.error(err);
    }

    const concatenatedContent = dataA + dataB;

    fs.writeFile(fileC, concatenatedContent, 'utf8', (err) => {
      if (err) {
        return console.error(err);
      }
    });
  });
});
