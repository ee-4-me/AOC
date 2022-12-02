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
      'X': 0,
      'Y': 3,
      'Z': 6,
    }

    const opp = {
      'AX' : 3,
      'BX' : 1,
      'CX' : 2,
      'AY' : 1,
      'BY' : 2,
      'CY' : 3,
      'AZ' : 2,
      'BZ' : 3,
      'CZ' : 1,
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