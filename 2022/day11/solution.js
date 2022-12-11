const fs = require('fs');
const path = require('path');

const sc = '\r\n';
  
const run = async (part) => {
  return new Promise ((resolve, reject) => {
    // fs.readFile(path.join(__dirname, './test.txt'), 'utf8', (err, data) => {
    fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
      if (err) throw err;
      // ----------------

      data = data.split(sc + sc);
      let monks = [];
      let primeMult = 1;

      // put input data into an array of objects, very hard coded lol
      for (const group of data) {
        let g = group.split(sc);
        let mo = {};
        let a = [];
        let t = g[1].split(' ');
        for (let i = 4; i < t.length; i++) {
          t[i] = t[i].replace(',', '');
          a.push(Number(t[i]));
        }
        mo.throws = 0;
        mo.worryArr = a;
        let x = g[2].split(' ');
        mo.eqn = x[5] + ' ' + x[6] + ' ' + x[7];
        mo.eqn = `${x[5]} ${x[6]} ${x[7]}`;
        mo.divide = Number(g[3].split(' ')[5]);
        primeMult *= mo.divide;
        mo.t = Number(g[4].split(' ')[9]);
        mo.f = Number(g[5].split(' ')[9]);
        monks.push(mo);
      }

      for (let c = 0; c < (part === 1 ? 20 : 10000); c++) {
        for (let i = 0; i < monks.length; i++) {
          let monk = monks[i];
          for (let j = 0; j < monk.worryArr.length; j) {
            monks[i].throws++;
            let worry = monk.worryArr[j];

            // hehe eval
            worry = eval(monk.eqn.replaceAll('old', worry.toString()));

            if (part === 1) {
              worry = Math.floor(worry / 3)
            } else {
              worry = worry % primeMult;
            }

            if (worry % monk.divide === 0) {
              monks[monk.t].worryArr.push(worry);
            } else {
              monks[monk.f].worryArr.push(worry);
            }

            monks[i].worryArr.shift();
          }
        }
      }

      monks.sort((b, a) => a.throws - b.throws);

      resolve(monks[0].throws * monks[1].throws)
      // -----------------
    });
  });
}

const solve = async () => {
  console.log(`Part 1: ${await run(1)}`); 
  console.log(`Part 2: ${await run(2)}`); 
}

solve();