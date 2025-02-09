#!/usr/bin/node
function factorial (n) {
  if (n <= 1) {
    return 1;
  } else {
    return factorial(n - 1) * n;
  }
}

const num = Number.isNaN(Number(process.argv[2])) ? 0 : Number(process.argv[2]);
console.log(factorial(num));
