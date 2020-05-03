// implementation of insertion sort in JavaScript on an arr of integers

const arr = [100, 6, 34, 78, 2, 100, 10000, 5, 789];

const insertionSort  = (arr) => {
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
