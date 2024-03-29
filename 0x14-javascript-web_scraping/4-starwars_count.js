#!/usr/bin/node
const request = require('request');
const address = process.argv[2];

request(address, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const i in results) {
      for (const chr of results[i].characters) {
        if (chr.search('/18/') > 0) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
