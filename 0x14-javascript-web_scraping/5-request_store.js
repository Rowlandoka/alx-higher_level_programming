#!/usr/bin/node
const request = require('request');
const address = process.argv[2];

request(address, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const fs = require('fs');
    fs.writeFile(process.argv[3], body, function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});
