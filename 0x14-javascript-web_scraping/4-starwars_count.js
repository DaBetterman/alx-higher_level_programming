#!/usr/bin/node
/**
 * Prints the number of movies where the character "Wedge Antilles" is present.
 * @param {string} apiUrl - The API URL of the Star Wars API films endpoint.
 */

const request = require('request');

function countMoviesWithCharacter (apiUrl) {
  const characterId = 18; // Wedge Antilles' character ID
  const url = `${apiUrl}${characterId}`;

  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const films = JSON.parse(body).films;
      console.log(films.length);
    }
  });
}

const apiUrl = process.argv[2];
countMoviesWithCharacter(apiUrl);
