const fs = require('fs');
const path = require('path');

const hs = (a, b) => {
  return `${a} ${b}`;
}

const run = async () => {
  // fs.readFile(path.join(__dirname, './test.txt'), 'utf8', (err, data) => {
  fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
    if (err) throw err;
    // ----------------

    // let grid = [];
    // for (let i = 0; i < 50; i++) {
    //   let g = [];
    //   for (let j = 0; j < 50; j++) {
    //     g.push(' ');
    //   }
    //   grid.push(g);
    // }
    // let height = 10;
    let height = 2000000;

    data = data.split('\r\n');

    let P = {};

    for (const lineIndex in data) {
      console.log(lineIndex, data.length);
      const line = data[lineIndex];
      const xs = Number(line.split('x=')[1].split(',')[0]);
      const ys = Number(line.split('y=')[1].split(':')[0]);
      const xb = Number(line.split('x=')[2].split(',')[0]);
      const yb = Number(line.split('y=')[2].split(',')[0]);
      P[hs(ys, xs)] = 'S';
      P[hs(yb, xb)] = 'B';

      let d = Math.abs(ys - yb) + Math.abs(xs - xb);

      if (ys + d < height) continue;
      if (ys - d > height) continue;

      let dy = Math.abs(height - ys);
      let dx = Math.abs(d - dy);

      for (let j = xs - dx; j <= xs + dx; j++) {
        let s = hs(height, j);
        if (P[s] === undefined) P[s] = 'C';
      }

      // for (let i = ys - d; i <= ys + d; i++) {
      //   let o = d - Math.abs(i - ys);
      //   for (let j = xs - o; j <= xs + o; j++) {
      //     let s = hs(i, j);
      //     if (P[s] === undefined) P[hs(i, j)] = 'C';
      //   }
      // }
    }

    // console.log(P);
    let ans = 0;

    for (const prop in P) {
      let s = prop;
      let i = Number(s.split(' ')[0]);
      if (i === height && P[prop] === 'C') ans++;
    }

    console.log(ans);

    // for (const prop in P) {
    //   let s = prop;
    //   let i = Number(s.split(' ')[0]);
    //   let j = Number(s.split(' ')[1]);
    //   grid[i + 20][j + 20] = P[prop];
    // }

    // for (const r of grid) {
    //   for (const c of r) {
    //     process.stdout.write(c);
    //   }
    //   process.stdout.write('\n');

    // }




    // -----------------
  });
}

run();