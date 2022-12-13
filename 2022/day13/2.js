const fs = require('fs');
const path = require('path');

const sc = '\r\n';

const compare = (l, r, i) => {
  l = JSON.parse(JSON.stringify(l));
  r = JSON.parse(JSON.stringify(r));
  i = JSON.parse(JSON.stringify(i));

  if (!Array.isArray(l)) l = [l];
  if (!Array.isArray(r)) r = [r];

  while (i < Math.max(l.length, r.length)) {
    if (l[i] === undefined && r[i] !== undefined) {
      return 1;
    } else if (r[i] === undefined && l[i] !== undefined) {
      return -1;
    } else if (l[i] === undefined && r[i] === undefined) {
      return 1;
    } else if (!Array.isArray(l[i]) && !Array.isArray(r[i])) { // both numbers
      if (l[i] > r[i]) return -1;
      if (l[i] < r[i]) return 1;
    } else {
      if (!Array.isArray(l[i])) l[i] = [l[i]];
      if (!Array.isArray(r[i])) r[i] = [r[i]];

      let c = compare(l[i], r[i], 0);
      if (c == 1) return 1;
      if (c == -1) return -1;
    }
    i++;
  }

  return 0
}
  
const run = async () => {
  fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
    if (err) throw err;
    // ----------------

    data = data.split(sc + sc);

    let a = [];

    for (const gi in data) {
      const group = data[gi].split(sc);
      let l = JSON.parse(group[0]);
      let r = JSON.parse(group[1]);
      a.push(l);
      a.push(r);
    }

    a.push([[2]]);
    a.push([[6]]);

    a.sort((l, r) => compare(r, l, 0)); // amazing sort method thank you javacript

    let ans = 1;

    for (let i = 0; i < a.length; i++) {
      if (a[i][0] !== undefined) {
        if (a[i][0][0] === 2 && a[i][0][1] === undefined && a[i][1] === undefined) ans *= (i + 1);
      }
      if (a[i][0] !== undefined) {
        if (a[i][0][0] === 6 && a[i][0][1] === undefined && a[i][1] === undefined) ans *= (i + 1);
      }
    }

    console.log(ans);
    // -----------------
  });
}

run();