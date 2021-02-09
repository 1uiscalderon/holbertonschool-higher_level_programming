#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const users = {};
    for (const todo of todos) {
      if (todo.completed === true) {
        if (todo.userId in users) {
          users[todo.userId] += 1;
        } else {
          users[todo.userId] = 1;
        }
      }
    }
    console.log(users);
  }
});
