#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, res, body) => {
    if(!err) {
        let count = 0;
        for (const film of JSON.parse(body).results) {
            for (const character of film.characters) {
                if (character.includes('18')) count++;
            }
        }
        return count;
    }
});