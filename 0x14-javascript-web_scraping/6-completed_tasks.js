#!/usr/bin/node
/**
 * Computes the number of tasks completed by user id.
 * @param {string} apiUrl - The API URL of the JSONPlaceholder todos endpoint.
 */

const request = require('request');

function countCompletedTasks (apiUrl) {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const todos = JSON.parse(body);
      const completedTasksByUser = {};

      todos.forEach((todo) => {
        if (todo.completed) {
          if (completedTasksByUser[todo.userId]) {
            completedTasksByUser[todo.userId]++;
          } else {
            completedTasksByUser[todo.userId] = 1;
          }
        }
      });

      console.log(completedTasksByUser);
    }
  });
}

const apiUrl = process.argv[2];
countCompletedTasks(apiUrl);
