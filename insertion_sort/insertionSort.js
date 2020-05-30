const arr = [100, 6, 34, 78, 2, 100, 10000, 5, 789];

// iterative implementation of insertion sort in JS on an arr of integers
const insertionSort = (arr) => {
  for (let i = 0; i < arr.length; i++) {
    let current = arr[i];
    let j = i;
    while (j > 0 && arr[j - 1] > current) {
      arr[j] = arr[j - 1];
      j -= 1;
    }
    arr[j] = current;
  }
  return arr;
}

console.log(insertionSort(arr));

// recursive implementation of insertion sort in JS on an arr of integers
const sort = (arr, n) => {
  if (n <= 1) {
    return arr;
  }
  sort(arr, n - 1);

  for (let i = 0; i < arr.length; i++) {
    let current = arr[i];
    let j = i;
    while (j > 0 && arr[j - 1] > current) {
      arr[j] = arr[j - 1];
      j -= 1;
    }
    arr[j] = current;
  }
  return arr;
}

const recursiveInsertionSort = (arr) => {
  const n = arr.length;
  return sort(arr, n);
}

console.log(recursiveInsertionSort(arr));
