const fs = require('fs');
const path = require('path');

const run = async () => {
  fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
    if (err) throw err;

    let ans_p1 = 0;
    let ans_p2 = 0;

    data = data.split('\r\n');

    let grid_p1 = [];

    for (const line of data) {
      let x1 = Number(line.split(',')[0].split(' ')[1]);
      let y1 = Number(line.split(',')[1].split(' ')[0]);
      let x2 = Number(line.split(',')[1].split(' ')[2]);
      let y2 = Number(line.split(',')[2]);
      console.log(line);
      console.log(x1, y1, x2, y2);
    }



    console.log(`Part 1: ${ans_p1}`);
    console.log(`Part 2: ${ans_p2}`);
  });
}

run();