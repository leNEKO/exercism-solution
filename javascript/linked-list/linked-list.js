class Node {
  constructor(data) {
    this.data = data;
    this.next = undefined;
  }
}

// a singly linked list implementation, will try with doubly next
class LinkedList {
  constructor() {
    this.head = undefined;
  }

  push(data) {
    if (this.head === undefined) {
      this.head = new Node(data);
      return;
    }

    let current = this.head;
    while (current.next !== undefined) {
      current = current.next;
    }
    current.next = new Node(data);
  }

  pop() {
    let current = this.head;
    if (this.head.next === undefined) {
      this.head = undefined;
      return current.data;
    }

    while (current.next.next !== undefined) {
      current = current.next;
    }
    let end_node = current.next;
    current.next = undefined;
    return end_node.data;
  }

  unshift(data) {
    let newHead = new Node(data);
    newHead.next = this.head;
    this.head = newHead;
  }

  shift() {
    let current = this.head;
    this.head = current.next;
    return current.data;
  }

  count() {
    if (this.head === undefined) {
      return 0;
    }
    var i = 1;
    let current = this.head;
    while (current.next !== undefined) {
      current = current.next;
      i++;
    }

    return i;
  }

  delete(data) {
    if (this.head === undefined) {
      return;
    }
    if (this.head.data === data) {
      this.shift();
      return;
    }

    let current = this.head;
    while (current.next !== undefined) {
      if (current.next.data === data) {
        current.next = current.next.next;
        return;
      }
      current = current.next;
    }
    current.next = new Node(data);
  }
}

module.exports = LinkedList;

if (require.main === module) {
  var node = new LinkedList();
  var list = new LinkedList();
  list.push(10);
  list.push(20);
  list.push(10);
  list.push(30);
  list.delete(10);
  console.log(list);
}
