const fs = require('fs');
const path = require('path');
let data = require('./input.js');

data = data.split('\n\n');

let o = [];

for (const group of data) {
  let sum = 0;
  let arr = group.split('\n');
  for (const cal of arr) {
    sum += Number(cal);
  }
  o.push(sum);
}

o.sort((a, b) => b - a);

console.log(o[0] + o[1] + o[2]);