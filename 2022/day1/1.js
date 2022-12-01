const fs = require('fs');
const path = require('path');
let data = require('./input.js');

data = data.split('\n\n');

let max = 0;

for (const group of data) {
  let sum = 0;
  let arr = group.split('\n');
  for (const cal of arr) {
    sum += Number(cal);
  }
  max = Math.max(max, sum);
}

console.log(max);