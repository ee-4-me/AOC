const fs = require('fs');
const path = require('path');

const run = async () => {
  fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
    if (err) throw err;

    let ans_p1 = 0;
    let ans_p2 = 0;

    data = data.split('\r\n');

    for (const line of data) {
      let vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0};
      for (const c of line) {
        if (vowels[c] !== undefined) vowels[c]++;
      }
      let nvowels = 0;
      for (const prop in vowels) {
        nvowels += vowels[prop];
      }
      if (nvowels < 3) continue;
      if (line.includes('ab')) continue;
      if (line.includes('cd')) continue;
      if (line.includes('pq')) continue;
      if (line.includes('xy')) continue;

      for (let i = 1; i < line.length; i++) {
        if (line[i] === line[i - 1]) {
          ans_p1++;
          break;          
        }
      }
    }

    for (const line of data) {

      let valid = false;
      for (let i = 1; i < line.length; i++) {
        let s1 = line[i - 1] + line[i];
        for (let j = i + 2; j < line.length; j++) {
          if (s1 === line[j - 1] + line[j]) {
            valid = true;
            break;
          }
        }
      }

      if (!valid) continue;

      for (let i = 2; i < line.length; i++) {
        if (line[i] === line[i - 2]) {
          ans_p2++;
          break;          
        }
      }
    }

    console.log(`Part 1: ${ans_p1}`);
    console.log(`Part 2: ${ans_p2}`);
  });
}

run();