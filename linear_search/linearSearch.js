// recursive linear search implementation
const search = (v, l, item) => {
  const n = v.length;
  if (l > n) {
    return false;
  }
  if (v[l] === item) {
    return true;
  }
  return search(v, l + 1, item);
}

const linearSearch = (v, item) => {
  return search(v, 0, item);
}

console.log(linearSearch([1, 5, 10, 79, 30, 6], 6));
