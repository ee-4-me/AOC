const fs = require('fs');
const path = require('path');

const sc = '\r\n';
  
const run = async () => {
  // fs.readFile(path.join(__dirname, './test.txt'), 'utf8', (err, data) => {
  fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
    if (err) throw err;
    // ----------------

    data = data.split(sc);

    let grid = [];

    for (const line of data) {
      let a = [];
      for (const char of line) {
        a.push(Number(char));
      }
      grid.push(a);
    }

    let max = 0;
    // each col left to right
    for (let i = 0; i < grid.length; i++) {
      for (let j = 0; j < grid[i].length; j++) {
        // will have i, j for each spot that needs to be checked
        let h = grid[i][j];

        let d = 0;
        let u = 0;
        let r = 0;
        let l = 0;
        
        for (let ii = i + 1; ii < grid.length; ii++) { // looking down
          d++;
          if (grid[ii][j] >= h) break;
        }

        for (let ii = i - 1; ii >= 0; ii--) { // looking up
          u++;
          if (grid[ii][j] >= h) break;
        }

        for (let jj = j + 1; jj < grid[i].length; jj++) { // looking right
          r++;
          if (grid[i][jj] >= h) break;
        }

        for (let jj = j - 1; jj >= 0; jj--) { // looking left
          l++;
          if (grid[i][jj] >= h) break;
        }

        max = Math.max(max, d * u * l * r);
      }
    }


    console.log(max);
    // -----------------
  });
}

run();