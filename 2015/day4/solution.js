const fs = require('fs');
const path = require('path');
const md5 = require('md5');

const run = async () => {
  fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
  // fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
    if (err) throw err;

    let ans_p1 = 0;
    let ans_p2 = 0;


    for (ans_p1; ans_p1 < ans_p1 + 1; ans_p1++) {
      let msg = md5(`${data}${ans_p1}`);
      
      let i = 0;
      for (i; i < msg.length; i++) {
        if (msg[i] !== '0') break;
      }
      if (i === 5) break;
    }

    ans_p2 = ans_p1 - 1;

    for (ans_p2; ans_p2 < ans_p2 + 1; ans_p2++) {
      let msg = md5(`${data}${ans_p2}`);
      
      let i = 0;
      for (i; i < msg.length; i++) {
        if (msg[i] !== '0') break;
      }
      if (i === 6) break;
    }

    console.log(`Part 1: ${ans_p1}`);
    console.log(`Part 2: ${ans_p2}`);
  });
}

run();