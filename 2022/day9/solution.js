const fs = require('fs');
const path = require('path');
  
const run = async (n) => {
  return new Promise ((resolve, reject) => {
    fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
      if (err) throw err;

      data = data.split('\r\n');

      let hash = {};

      let a = [];
      for (let i = 0; i < n; i++) { // make rope
        a.push([0, 0]);
      }

      for (const line of data) {
        const args = line.split(' ');
        const l = args[0];
        const n = Number(args[1]);

        for (let i = 0; i < n; i++) {
        
          // move the head
          if (l === 'R') {
            a[0][1]++;
          } else if (l === 'L') {
            a[0][1]--;
          } else if (l === 'U') {
            a[0][0]--;
          } else {
            a[0][0]++;
          }

          hash[`${a[a.length - 1][0]} ${a[a.length - 1][1]}`] = 0; // store the position of the tail in a "hash"
          
          // for everything after the head, move them acording to the rules
          for (let i = 1; i < a.length; i++) {
            if (Math.abs(a[i - 1][0] - a[i][0]) >= 2 || Math.abs(a[i - 1][1] - a[i][1]) >= 2) { // issue
              if (a[i - 1][1] === a[i][1]) {
                if (a[i - 1][0] > a[i][0]) {
                  a[i][0]++;
                } else {
                  a[i][0]--;
                }
              } else if (a[i - 1][0] === a[i][0]) {
                if (a[i - 1][1] > a[i][1]) {
                  a[i][1]++;
                } else {
                  a[i][1]--;
                }
              } else {
                if (a[i - 1][0] > a[i][0]) {
                  a[i][0]++;
                } else {
                  a[i][0]--;
                }
                if (a[i - 1][1] > a[i][1]) {
                  a[i][1]++;
                } else {
                  a[i][1]--;
                }
              }
            }
          }
        }
      }

      let ans = 0;
      for (const prop in hash) { // count unique positions
        ans++;
      }

      resolve(ans);
    });
  });
}

const solve = async () => {
  console.log(`Part 1: ${await run(2)}`); 
  console.log(`Part 2: ${await run(10)}`); 
}

solve();