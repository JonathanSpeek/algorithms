// recursive implementation of computing the greatest common divisor (Euclidean algorithm)
const gcd = (a, b) => {
  if (b === 0) {
    return a;
  }
  return gcd(b, a % b);
}

console.log(gcd(2, 9));
