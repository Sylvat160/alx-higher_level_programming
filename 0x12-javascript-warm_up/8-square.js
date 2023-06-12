#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (process.argv.length === 2) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
