const fs = require('fs');
const path = require('path');

const sc = '\r\n';

let ans = [];
let o;
let index = 0;

let add = (a) => {
  let sum = 0;
  if (a[1] !== undefined) {
    for (let i = 0; i < a[1].length; i++) {
      sum += Number(a[1][i].split(' ')[0]);
    }
  }
  if (a[2] !== undefined) {
    for (let i = 0; i < a[2].length; i++) {
      sum += add(a[2][i]); 
    }
  }
  ans.push(sum);
  return sum;
}

const search = (a) => {
  while (index < lines.length) {
    index++;
    if (index >= lines.length) break;
    const line = lines[index];
    const args = line.split(' ');

    if (line === '$ cd ..') return a; // back out

    if (args[0] === '$' && args[1] === 'cd') { // find the dir, then search it
      for (let j = 0; j < a[2].length; j++) {
        if (a[2][j][0] === args[2]) {
          a[2][j] = search(a[2][j]);
          break;
        }
      }
    }

    if (!isNaN(Number(args[0]))) {
      if (a[1] === undefined) a[1] = [];
      a[1].push(line);
    }
    if (args[0] === 'dir') {
      if (a[2] === undefined) a[2] = [];
      a[2].push([args[1]])
    }
  }
  return a; // last one
}

const run = () => {
  // fs.readFile(path.join(__dirname, './test.txt'), 'utf8', async (err, data) => {
  fs.readFile(path.join(__dirname, './input.txt'), 'utf8', async (err, data) => {
    if (err) throw err;
    // ----------------

    lines = await data.split(sc);
    o = search(['/']);
    add(o);

    // let sum = 0;

    // // dirs have same name!
    // for (const n of ans) {
    //   if (n < 100000) {
    //     sum += n;
    //   }
    // }
    ans.sort((a, b) => a - b);

    let max = 70000000;
    let need = 30000000;
    let used = ans[ans.length - 1];
    let unused = max - used;

    for (const n of ans) {
      if (unused + n >= need) {
        console.log(n);
        break;
      }
    }

    // -----------------
  });
}

run();
