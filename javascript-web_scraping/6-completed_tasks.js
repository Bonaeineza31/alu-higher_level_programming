#!/usr/bin/node
const [, , URL] = process.argv;
require('request')(URL, (_, __, body) => {
  console.log(JSON.parse(body).reduce((acc, usr) => {
    return usr.completed
      ? {
          ...acc,
          [usr.userId]: (acc[usr.userId] || 0) + 1
        }
      : acc;
  }, {}));
});