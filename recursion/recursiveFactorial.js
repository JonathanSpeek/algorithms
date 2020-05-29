// recursive implementation of computing a factorial
const factorial = (n) => {
  if (n === 0) { return 1; }

  return n * factorial(n - 1);
}

console.log(factorial(9));
