const fs = require('fs');
const path = require('path');

const run = async () => {
  // fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
  fs.readFile(path.join(__dirname, './test.txt'), 'utf8', (err, data) => {
    if (err) throw err;

    let ans_p1 = 0;
    let ans_p2 = 0;

    data = data.split('\r\n');

    for (const line of data) {
      console.log(line);
    }

    console.log(`Part 1: ${ans_p1}`);
    console.log(`Part 2: ${ans_p2}`);
  });
}

run();