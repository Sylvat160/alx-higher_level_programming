#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  const arr = args.slice(2).map(Number);
  const max = Math.max(...arr);
  const secondMax = arr.filter(num => num !== max);
  console.log(Math.max(...secondMax));
}
