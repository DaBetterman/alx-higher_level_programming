#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie.
 * @param {number} movieId - The Movie ID.
 */

const request = require('request');

function getCharactersInMovie (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const movie = JSON.parse(body);
      const characters = movie.characters;

      characters.forEach((characterUrl) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            console.error(error);
          } else {
            const character = JSON.parse(body);
            console.log(character.name);
          }
        });
      });
    }
  });
}

const movieId = process.argv[2];
getCharactersInMovie(movieId);
