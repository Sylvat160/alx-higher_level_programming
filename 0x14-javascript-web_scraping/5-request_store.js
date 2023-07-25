#!/usr/bin/node
const request = require('request');
const fs = require('fs');
// request(process.argv[2], (err, res, body) => {
//     if (!err) {
//         fs.writeFile(process.argv[3], body, 'utf8', err => {
//             if (err) console.log(err);
//         });
//     }
// });
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));