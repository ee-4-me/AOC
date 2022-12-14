const fs = require('fs');
const path = require('path');

const sc = '\r\n';

let c = 0;

const placeOne = (grid, i, j) => {
  if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length) return null;

  for (i; i < grid.length - 1; i++) {
    if (grid[i][j] === '.') {
      if (grid[i + 1][j - 1] !== '.' && grid[i + 1][j] !== '.' && grid[i + 1][j + 1] !== '.') {
        grid[i][j] = 'o';
        c++;
        return grid;
      } else if (grid[i + 1][j] !== '.') {
        if (grid[i + 1][j - 1] === '.') {
          j--;
        } else if (grid[i + 1][j + 1] === '.') {
          j++;
        }
      }
    } else {
      return null;
    }
  }

  return null;
}
  
const run = async () => {
  fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
    if (err) throw err;

    data = data.split(sc);

    let grid = [];
    for (let i = 0; i < 1000; i++) {
      let gg = [];
      for (let j = 0; j < 1000; j++) {
        gg.push('.');
      }
      grid.push(gg);
    }

    for (const line of data) {
      let t = line.split(' -> ');
      let a = [];
      for (const tt of t) {
        let ttt = tt.split(',');
        a.push([Number(ttt[1]), Number(ttt[0])]); // flip so it is i, j
      }

      for (let i = 1; i < a.length; i++) {
        let prev = a[i - 1];
        let curr = a[i];
        if (prev[0] === curr[0]) { // same height, doing left to right
          for (let j = Math.min(prev[1], curr[1]); j <= Math.max(prev[1], curr[1]); j++) {
            grid[prev[0]][j] = '#';
          }
        } else { // different height, doing top to bottom
          for (let j = Math.min(prev[0], curr[0]); j <= Math.max(prev[0], curr[0]); j++) {
            grid[j][prev[1]] = '#';
          }
        }
      }
    }

    // falling sand
    while (grid !== null) {
      grid = placeOne(grid, 0, 500);
    }

    console.log(c);
  });
}

run();