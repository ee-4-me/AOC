const fs = require('fs');
const path = require('path');

const sc = '\r\n';

const run = async () => {
  fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
    if (err) throw err;

    data = data.split(sc + sc);

    let o = [];

    for (const group of data) {
      let sum = 0;
      let arr = group.split('\n');
      for (const cal of arr) {
        sum += Number(cal);
      }
      o.push(sum);
    }

    o.sort((a, b) => b - a);

    console.log(o[0] + o[1] + o[2]);
  
  });
}

run();