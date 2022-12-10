const fs = require('fs');
const path = require('path');

const sc = '\r\n';
  
const run = async () => {
  // fs.readFile(path.join(__dirname, './test.txt'), 'utf8', (err, data) => {
  fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
    if (err) throw err;
    // ----------------

    data = data.split(sc);

    let x = 1;

    let o = [];

    for (const line of data) {
      let args = line.split(' ');
      let l = args[0];
      let n = Number(args[1]);

      if (l === 'addx') {
        o.push(x);
        o.push(x);
        x += n;
      } else {
        o.push(x);
      }

    }


    let ans = 0;
    for (let i = 20; i <= 220; i += 40) {
      ans += o[i - 1] * i;
      console.log(o[i - 1], i);
    }

    console.log(ans);

    // -----------------
  });
}

run();