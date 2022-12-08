const fs = require('fs');
const path = require('path');

const sc = '\r\n';
  
const run = async () => {
  // fs.readFile(path.join(__dirname, './test.txt'), 'utf8', (err, data) => {
  fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => {
    if (err) throw err;
    // ----------------

    data = data.split(sc);

    let grid = [];

    for (const line of data) {
      let a = [];
      for (const char of line) {
        a.push(Number(char));
      }
      grid.push(a);
    }
    let ag = JSON.parse(JSON.stringify(grid));

    for (let i = 0; i < ag.length; i++) {
      for (let j = 0; j < ag[i].length; j++) {
        if (i === 0 || i === ag.length - 1 || j === 0 || j == ag[i].length - 1) {
          ag[i][j] = 1;          
        } else {
          ag[i][j] = 0;
        }
      }
    }

    // each col left to right
    for (let i = 1; i < grid.length - 1; i++) {
      let cmax = grid[i][0];
      for (let j = 1; j < grid[i].length - 1; j++) {
        if (grid[i][j] > cmax) ag[i][j] = 1;
        cmax = Math.max(cmax, grid[i][j]);
      }

      cmax = grid[i][grid[i].length - 1];
      for (let j = grid[i].length - 2; j >= 1; j--) {
        if (grid[i][j] > cmax) ag[i][j] = 1;
        cmax = Math.max(cmax, grid[i][j]);
      }
    }

    // each row top to bottom
    for (let j = 1; j < grid[0].length - 1; j++) {
      let rmax = grid[0][j];
      for (let i = 1; i < grid.length - 1; i++) {
        if (grid[i][j] > rmax) ag[i][j] = 1;
        rmax = Math.max(rmax, grid[i][j]);
      }

      rmax = grid[grid.length - 1][j];
      for (let i = grid.length - 2; i >= 1; i--) {
        if (grid[i][j] > rmax) ag[i][j] = 1;
        rmax = Math.max(rmax, grid[i][j]);
      }
    }
    
    let sum = 0;

    for (const row of ag) {
      for (const bit of row) {
        sum += bit;
      }
    }

    console.log(sum);
    // -----------------
  });
}

run();