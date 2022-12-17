const fs = require('fs');
const path = require('path');

const run = async () => {
  fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
    if (err) throw err;

    data = data.split('\r\n');

    let sa = 0;
    let r = 0;

    for (const line of data) {
      let args = line.split('x').map((e) => Number(e));
      const l = args[0];
      const w = args[1];
      const h = args[2];

      sa += 2 * (l*w + l*h + w*h) + Math.min(l*w, l*h, w*h);
      r += (2 * Math.min(l + w, l + h, h + w)) + (l * w * h);
    }
    
    console.log(`Part 1: ${sa}`);
    console.log(`Part 2: ${r}`);
  });
}

run();