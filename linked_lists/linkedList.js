// basic linked list Node class
class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

let head = new Node(4);
head.next = new Node(6);
head.next.next = new Node(10);

// linear search of linked list
const search = (head, item) => {
  let temp = head;
  while (temp !== null) {
    if (temp.data === item) return true;
    temp = temp.next;
  }
  return false;
}

console.log(search(head, 7));
console.log(search(head, 6));

