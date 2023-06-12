#!/usr/bin/node
const args = process.argv;
function factorial (a) {
  return a === 0 || isNaN(a) ? 1 : a * factorial(a - 1);
}

console.log(factorial(parseInt(args[2])));
