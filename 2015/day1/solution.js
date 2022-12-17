const fs = require('fs');
const path = require('path');

let hash = {'(': 1, ')': -1};
  
const run = async () => {
  fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
    if (err) throw err;

    let ans = 0;
    let index = -1;

    for (let i = 0; i < data.length; i++) {
      if (index === -1 && ans < 0) index = i;
      ans += hash[data[i]];
    }
    
    console.log(`Part 1: ${ans}`);
    console.log(`Part 2: ${index}`);
  });
}

run();