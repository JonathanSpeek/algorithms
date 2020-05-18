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
  if (arr.length < 1) return 'Item not found in the arr.';

  let right = arr.length;
  let left = 0;
  let middle = Math.floor((left + right) / 2);

  if (arr[middle] === item) {
    return `Found at position ${middle}.`;
  }

  if (arr[middle] < item) {
    return binarySearchRecursive(array.slice(middle + 1, right), item);
  } else {
    return binarySearchRecursive(array.slice(left, middle), item);
  }
}

console.log(binarySearch(arr, 4));
