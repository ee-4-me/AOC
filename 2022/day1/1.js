const fs = require('fs');
const path = require('path');

const sc = '\r\n';

const run = async () => {
  fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
    if (err) throw err;

    data = data.split(sc + sc);

    let max = 0;
  
    for (const group of data) {
      let sum = 0;
      let arr = group.split(sc);
      for (const cal of arr) {
        sum += Number(cal);
      }
      max = Math.max(max, sum);
    }
  
    console.log(max);
  
  });
}

run();