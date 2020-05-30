// iterative implementation of bubble sort in JS on an array of integers

const arr = [100, 6, 34, 78, 2, 100, 10000, 5, 789];

const bubbleSort = (arr) => {
  arr.forEach(() => {
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] > arr[i + 1]) {
        [arr[i], arr[i+1]] = [arr[i+1], arr[i]];
      }
    }
  });
  return arr;
}

console.log(bubbleSort(arr));


// recursive implementation of bubble sort in JS on an array of integers
const sort = (arr, n) => {
  if (n === 1) {
    return arr;
  }
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > arr[i + 1]) {
      [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
    }
  }
  return sort(arr, n - 1);
};

const recursiveBubbleSort = (vector) => {
  const n = vector.length - 1;
  return sort(vector, n);
}

console.log(recursiveBubbleSort(arr, arr.length - 1));
