#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a
//  given integer
const request = require('request');
const [id] = process.argv.slice(2);
request(`https://swapi-api.alx-tools.com/api/films/${id}`, (err, res, body) => {
  if (err) console.error(err);
  console.log(JSON.parse(body).title);
});
