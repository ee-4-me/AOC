const fs = require('fs');
const path = require('path');

let shapes = [];
let grid = [];

let lineh = [[0, 0], [1, 0], [2, 0], [3, 0]];
let plus = [[0, 1], [1, 0], [1, 1], [1, 2], [2, 1]];
let l = [[0, 0], [1, 0], [2, 2], [2, 1], [2, 0]];
let linev = [[0, 1], [0, 2], [0, 3], [0, 0]];
let square = [[0, 0], [0, 1], [1, 1], [1, 0]];

let maxh = 4 * 2022 + 10;

shapes.push(lineh);
shapes.push(plus);
shapes.push(l);
shapes.push(linev);
shapes.push(square);

const print = () => {
  for (let i = grid.length - 1; i >= 0; i--) {
    const row = grid[i];
    for (const c of row) {
      process.stdout.write(c);
    }
    process.stdout.write('\n');
  }
}

const good = (shape, j, i) => {
  if (i < 0) return false;
  for (const point of shape) {
    let x = point[0];
    let y = point[1];
    if (j + x >= 7 || j < 0) return false;
    if (grid[i + y][j + x] !== '.') return false;
  }
  return true;
}

const add = (shape, j, i) => {
  for (const point of shape) {
    let x = point[0];
    let y = point[1];
    grid[i + y][j + x] = '#';
  }
}

const getHeight = () => {
  for (let i = 0; i < maxh; i++) {
    let valid = false;
    for (let j = 0; j < 7; j++) {
      if (grid[i][j] !== '.') {
        valid = true;
        break;
      }
    }
    if (!valid) return i;
  }
  return maxh;
}

const run = async () => {
  fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
    if (err) throw err;

    for (let i = 0; i < maxh; i++) {
      let r = [];
      for (let j = 0; j < 7; j++) {
        r.push('.');
      }
      grid.push(r);
    }


    let ci = 0;
    for (let index = 0; index < 2022; index++) {
      let shape = shapes[index % shapes.length];
      let top = getHeight();

      let i = 3 + top;
      let j = 2;

      while (true) {
        let c = data[ci % data.length];
        if (c === '<') {
          if (good(shape, j - 1, i)) j--;
        } else {
          if (good(shape, j + 1, i)) j++;
        }
        ci++;
        if (good(shape, j, i - 1)) {
          i--;
        } else {
          add(shape, j, i);
          break;
        }
      }
    }
    
    console.log(getHeight());
  });
}

run();