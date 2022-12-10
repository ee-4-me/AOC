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

    let tt = [];

    for (let i = 0; i < 6; i++) {
      let t = [];
      let ttt = [];
      for (let j = 0; j < 40; j++) {
        ttt.push('.');
      }
      tt.push(ttt);
    }

    for (let i = 0; i < 6 * 40; i++) {
      if (Math.abs(o[i] - i % 40) <= 1) tt[Math.floor(i / 40)][i % 40] = '#';
    }

    for (let i = 0; i < 6; i++) {
      for (let j = 0; j < 40; j++) {
        process.stdout.write(tt[i][j].toString());
      }
      process.stdout.write('\n');
    }

    // -----------------
  });
}

run();