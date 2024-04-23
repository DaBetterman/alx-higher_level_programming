#!/usr/bin/node
/**
 * Reads and prints the content of a file.
 * @param {string} filePath - The path to the file to be read.
 */

const fs = require('fs');

function readFileContent (filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }
  });
}
const filePath = process.argv[2];
readFileContent(filePath);
