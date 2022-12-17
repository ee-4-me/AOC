const fs = require('fs');
const path = require('path');

const sc = '\r\n';

let gvalves = [];
let hash = {};
let ihash = {};

let timeTotal = 30;
let max = 0;

const search = (valves, time, sum, index, arr) => {
  console.log(time);
  max = Math.max(max, sum);

  if (time > 30) return;

  for (let i = 0; i < valves.length; i++) {
    if (i === index) continue;

    let nvalve = valves[i];
    if (nvalve[1] > 0 && nvalve[2] === 0) { // if it has a value and it is off
      let d = hash[valves[index][0]][nvalve[0]] + 1;
      let tsum = sum;
      let ttime = time;
      let tvalves = JSON.parse(JSON.stringify(valves));
      let arrr = JSON.parse(JSON.stringify(arr));
      let tindex = i;
      tvalves[tindex][2] = 1;
      ttime += d;
      arrr.push([nvalve[0], ttime]);
      tsum += Math.max(0, nvalve[1] * (timeTotal - ttime)); // add the amount of pressure it will make
      search(tvalves, ttime, tsum, tindex, arrr);
    }
  }
}

const run = async () => {
  fs.readFile(path.join(__dirname, './test.txt'), 'utf8', (err, data) => {
  // fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
    if (err) throw err;
    // ----------------

    data = data.split(sc);


    let ii = 0;
    // parse inputs
    for (const line of data) {
      let v = [];
      v[0] = line.split(' ')[1]; // name
      v[1] = Number(line.split(' ')[4].split('=')[1].split(';')[0]); // val
      v[2] = 0; // not oppened
      let t = line.split(' valve')[1].split(' ');
      t.shift();
      for (let i = 0; i < t.length; i++) {
        t[i] = t[i].replace(',', '');
      } 
      v[4] = t;
      hash[v[0]] = {};
      hash[v[0]][v[0]] = 0;
      ihash[v[0]] = ii;
      ii++;
      gvalves.push(v);
    }

    // bfs
    for (let i = 0; i < gvalves.length; i++) {
      let search = [];
      for (const valve of gvalves[i][4]) {
        search.push([valve, 1]);
      } 
  
      let inode = gvalves[i];
      while (search.length > 0) {
        let top = search[0];
  
        for (const svalve of gvalves[ihash[top[0]]][4]) { // connecting
          if (hash[inode[0]][svalve] !== undefined) continue;
          hash[inode[0]][svalve] = top[1];
          search.push([svalve, top[1] + 1]);
        }
  
        hash[inode[0]][top[0]] = top[1];
        search.shift();
      }
    }


    search(gvalves, 0, 0, 0, [['AA', 0]]);


    console.log(max);
    // console.log(hash);
    // -----------------
  });
}
// 2107 is not it, answers is larger than 2107
// bigger than 2150

run();

