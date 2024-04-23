#!/usr/bin/node
/**
 * Prints the title of a Star Wars movie where the episode number matches a given integer.
 * @param {number} movieId - The movie ID to retrieve the title for.
 */

const request = require('request');

function getMovieTitle (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const movie = JSON.parse(body);
      console.log(movie.title);
    }
  });
}

const movieId = process.argv[2];
getMovieTitle(movieId);
