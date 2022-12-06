const fs = require('fs');
const path = require('path');

const sc = '\r\n';
  
const run = async () => {
  // fs.readFile(path.join(__dirname, './test.txt'), 'utf8', (err, data) => {
  fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
    if (err) throw err;
    // ----------------

    for (let i = 13; i < data.length; i++) {
      let hash = {};
      for (let j = 0; j < 14; j++) {
        if (hash[data[i - j]] === undefined) hash[data[i - j]] = 0;
      }
      let c = 0;
      for (const prop in hash) {
        c++;
      }

      if (c === 14) {
        console.log(i + 1)
        break;
      }
    }
    
    // -----------------
  });
}

run();