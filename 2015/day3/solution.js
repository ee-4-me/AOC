const fs = require('fs');
const path = require('path');

const DIR = {
  '^': [-1, 0],
  'v': [1, 0],
  '>': [0, 1],
  '<': [0, -1],
}

const hash_p1 = {};
const hash_p2 = {};

const run = async () => {
  fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
    if (err) throw err;

    let ans1 = 0;
    let ans2 = 0;

    let x_p1 = 0;
    let y_p1 = 0;

    let x_p2_1 = 0;
    let y_p2_1 = 0;
    
    let x_p2_2 = 0;
    let y_p2_2 = 0;

    for (let i = 0; i < data.length; i++) {
      let c = data[i];
      let dir = DIR[c];

      x_p1 += dir[0];
      y_p1 += dir[1];
      let s_p1 = `${x_p1} ${y_p1}`;
      hash_p1[s_p1] = 0;

      // part 2

      if (i & 1) {
        x_p2_1 += dir[0];
        y_p2_1 += dir[1];
      } else {
        x_p2_2 += dir[0];
        y_p2_2 += dir[1];
      }

      let s_p2_1 = `${x_p2_1} ${y_p2_1}`;
      hash_p2[s_p2_1] = 0;

      let s_p2_2 = `${x_p2_2} ${y_p2_2}`;
      hash_p2[s_p2_2] = 0;
    }
    
    console.log(`Part 1: ${Object.keys(hash_p1).length}`);
    console.log(`Part 2: ${Object.keys(hash_p2).length}`);
  });
}

run();