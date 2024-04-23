#!/usr/bin/node
/**
 * Fetches the contents of a webpage and stores it in a file.
 * @param {string} url - The URL to request.
 * @param {string} filePath - The file path to store the body response.
 */

const request = require('request');
const fs = require('fs');

function fetchAndStore (url, filePath) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      fs.writeFile(filePath, body, 'utf-8', (err) => {
        if (err) {
          console.error(err);
        } else {
          console.log(`Contents of ${url} stored in ${filePath} successfully!`);
        }
      });
    }
  });
}

const url = process.argv[2];
const filePath = process.argv[3];

fetchAndStore(url, filePath);
