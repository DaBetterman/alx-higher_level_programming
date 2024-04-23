#!/usr/bin/node
/**
 * Writes a string to a file.
 * @param {string} filePath - The path to the file to write to.
 * @param {string} content - The content to write to the file.
 */

const fs = require('fs');

function writeToFile (filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    } else {
      console.log('Saved!');
    }
  });
}

const filePath = process.argv[2];
const content = process.argv[3];

writeToFile(filePath, content);
