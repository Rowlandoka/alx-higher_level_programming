#!/usr/bin/node
const request = require('request');
const address = process.argv[2];

request(address, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const output = {};
    for (const ct of JSON.parse(body)) {
      if (ct.completed) {
        if (output[ct.userId] == undefined) {
          output[ct.userId] = 0;
        }
        output[ct.userId] += 1;
      }
    }
    console.log(output);
  }
});
