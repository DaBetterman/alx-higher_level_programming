#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie in the same order as the list "characters" in the /films/ response.
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
      const characterUrls = movie.characters;

      function fetchCharacter (characterUrl) {
        return new Promise((resolve, reject) => {
          request(characterUrl, (error, response, body) => {
            if (error) {
              reject(error);
            } else {
              const character = JSON.parse(body);
              resolve(character.name);
            }
          });
        });
      }

      Promise.all(characterUrls.map(fetchCharacter))
        .then((characters) => {
          characters.forEach((character) => {
            console.log(character);
          });
        })
        .catch((error) => {
          console.error(error);
        });
    }
  });
}

const movieId = process.argv[2];
getCharactersInMovie(movieId);
