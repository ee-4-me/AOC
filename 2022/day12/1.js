const fs = require('fs');
const path = require('path');

const sc = '\r\n';

let f = (c) => { return c.charCodeAt(0) - 97 }

const run = async () => {
  // fs.readFile(path.join(__dirname, './test.txt'), 'utf8', (err, data) => {
  fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
    if (err) throw err;
    // ----------------

    data = data.split(sc);

    let grid = [];

    for (const line of data) {
      let g = [];
      for (const c of line) {
        if (c === 'S') {
          g.push(-1);
        } else if (c === 'E') {
          g.push(26);
        } else {
          g.push( f(c));
        }
      }
      grid.push(g);
    }

    let is = 0;
    let js = 0;

    for (const ri in grid) {
      for (const ci in grid[ri]) {
        if (grid[ri][ci] === -1) {
          is = Number(ri);
          jk = Number(ci);
        }
      }
    }

    let hash = {};
    hash[`${is} ${js}`] = 0;

    let p = [[is, js, 0]];

    while (p.length > 0) {
      // l, r, u, d
      const x = [-1, 1, 0, 0];
      const y = [0, 0, -1, 1];

      const point = p[0];
      const i = point[0];
      const j = point[1];
      const d = point[2];

      for (let k = 0; k < 4; k++) {
        const jj = j + x[k];
        const ii = i + y[k];

        let hs = `${ii} ${jj}`;
        if (hash[hs] !== undefined) continue; // been here, go to next
        
        if (jj < 0 || jj >= grid[0].length) continue; // out of bounds
        if (ii < 0 || ii >= grid.length) continue;
    
        if (grid[i][j] + 1 < grid[ii][jj]) continue; // can take step
    
        if (grid[ii][jj] === 26) {
          console.log(d + 1);
          return;
        }
        
        hash[hs] = 0;
        p.push([ii, jj, d + 1]);
      }

      p.shift();
    }

    // -----------------
  });
}

run();