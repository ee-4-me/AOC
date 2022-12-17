const fs = require('fs');
const { get } = require('https');
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
  let t = getHeight();
  for (let i = t + 5; i >= Math.max(t - 20, 0); i--) {
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
  for (let i = grid.length - 1; i >= 0; i--) {
    for (let j = 0; j < 7; j++) {
      if (grid[i][j] !== '.') return i + 1;
    }
  }
  return 0;
}

let den = 1705;
let num = 2597;
let leftover = 1000000000000 % den;
let extra = 2393; // extra = part1(leftover) 

console.log('Ans: ', (Math.floor(1000000000000 / den) * num) + extra);

// for every whole group of 1705 shapes -> 2597 height

const run = async () => {
  fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
    if (err) throw err;

    let r = [];
    for (let j = 0; j < 7; j++) {
      r.push('.');
    }
    grid.push(['.', '.', '.', '.', '.', '.', '.']);
    grid.push(['.', '.', '.', '.', '.', '.', '.']);
    grid.push(['.', '.', '.', '.', '.', '.', '.']);
    grid.push(['.', '.', '.', '.', '.', '.', '.']);
    grid.push(['.', '.', '.', '.', '.', '.', '.']);
    grid.push(['.', '.', '.', '.', '.', '.', '.']);

    let ci = 0;
    let topprev = 0;
    let indexprev = 0;
    let c = 0;
    for (let index = 0; index < 1000000000000; index++) {
      grid.push(['.', '.', '.', '.', '.', '.', '.']);
      grid.push(['.', '.', '.', '.', '.', '.', '.']);

      let shape = shapes[index % shapes.length];
      let top = getHeight();

      // console.log(ci, data.length, ci % data.length);
      if (ci % data.length === 1) {
        if (c > 0) {
          console.log('denominator: ', index - indexprev);
          console.log('numerator: ', top - topprev);
          return;
        }
        c++;
        topprev = top;
        indexprev = index;
      }

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

    print();
    
    console.log(getHeight());



  });
}

run();