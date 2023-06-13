#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const destination = process.argv[4];

function concatFiles (fileA, fileB, destination) {
  const contentA = fs.readFileSync(fileA, 'utf8');
  const contentB = fs.readFileSync(fileB, 'utf8');
  const concatenatedContent = contentA + contentB;
  fs.writeFileSync(destination, concatenatedContent);
}

concatFiles(fileA, fileB, destination);
