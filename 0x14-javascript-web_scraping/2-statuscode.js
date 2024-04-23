#!/usr/bin/node
/**
 * Displays the status code of a GET request.
 * @param {string} url - The URL to request (GET).
 */

const request = require('request');

function displayStatusCode (url) {
  request(url, (error, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
}

const url = process.argv[2];
displayStatusCode(url);
