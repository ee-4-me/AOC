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

    let sum = 0;

    for (const line of data) {
      let t = line.split(',');
      let n11 = Number(t[0].split('-')[0]);
      let n12 = Number(t[0].split('-')[1]);
      let n21 = Number(t[1].split('-')[0]);
      let n22 = Number(t[1].split('-')[1]);

      if ((n21 >= n11 && n21 <= n12) || (n22 >= n11 && n22 <= n12) || (n11 >= n21 && n11 <= n22) || (n12 >= n21 && n12 <= n22)) sum++;
    }

    console.log(sum);


    // -----------------
  });
}

run();