const fs = require('fs');
const path = require('path');

const sc = '\r\n';
  
const run = async () => {
  fs.readFile(path.join(__dirname, './test.txt'), 'utf8', (err, data) => {
  // fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
    if (err) throw err;
    // ----------------

    data = data.split(sc);
    // data = data.split(sc + sc);
    // console.log(data);

    for (const line of data) {
      console.log(line);
    }
    
    // -----------------
  });
}

run();