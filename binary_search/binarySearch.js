const arr = [1,2,3,4,5,6,7,8,9];

// iterative implementation of binary search in JavaScript

const binarySearch = (arr, item) => {
  let right = arr.length;
  let left = 0;

  while (right >= left) {
    let middle = Math.floor((left + right) / 2);
    if (arr[middle] === item) {
      return `Found at position ${middle}.`;
    } else if (arr[middle] > item) {
      right = middle - 1;
    } else {
      left = middle + 1;
    }
  }
  return 'Item not found in the arr.';
}

console.log(binarySearch(arr, 9));


// recursive implementation of binary search in JavaScript

const binarySearchRecursive = (arr, item) => {
  const n = arr.length;
  const mid = Math.floor((n - 1) / 2);

  if (n === 0) return 'Item not found in the arr.';

  if (arr[mid] === item) {
    return true;
  }

  if (arr[mid] < item) {
    return binarySearchRecursive(arr.slice(mid + 1), item);
  } else {
    return binarySearchRecursive(arr.slice(0, mid), item);
  }
}

console.log(binarySearchRecursive(arr, 6));
