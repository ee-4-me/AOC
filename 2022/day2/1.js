const fs = require('fs');
const path = require('path');

const sc = '\r\n';

const run = async () => {
  // fs.readFile(path.join(__dirname, './test.txt'), 'utf8', (err, data) => {
  fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
      if (err) throw err;
    // ----------------

    data = data.split(sc);
    // data = data.split(sc + sc);
    // console.log(data);

    const hash = {
      'X': 1,
      'Y': 2,
      'Z': 3,
    }

    const opp = {
      'AX' : 3,
      'BX' : 0,
      'CX' : 6,
      'AY' : 6,
      'BY' : 3,
      'CY' : 0,
      'AZ' : 0,
      'BZ' : 6,
      'CZ' : 3,
    }

    let sum = 0;
    
    for (const line of data) {
      let l = line.split(' ');
      sum += opp[l[0] + l[1]];
      sum += hash[l[1]]
    }

    console.log(sum);

    // -----------------
  });
}

run();