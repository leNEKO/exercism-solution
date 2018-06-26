class Node {
  constructor(data) {
    this.prev = null;
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  push(data) {
    let node = new Node(data);
    if (this.length > 0) {
      node.prev = this.tail;
      this.tail.next = node;
    } else {
      this.head = node;
    }
    this.length++;
    this.tail = node;
  }

  pop() {
    let data = this.tail.data;
    if (this.length > 1) {
      this.tail = this.tail.prev;
      this.tail.next = null;
    } else {
      this.tail = null;
    }
    this.length--;
    return data;
  }

  unshift(data) {
    let node = new Node(data);
    if (this.length < 1) {
      this.tail = node;
    } else {
      node.next = this.head;
      this.head.prev = node;
    }
    this.length++;
    this.head = node;
  }

  shift() {
    let data = this.head.data;
    this.head = this.head.next;
    this.length--;
    return data;
  }

  count() {
    return this.length;
  }

  delete(data) {
    let current = this.head;
    for (var i = 0; i < this.length; i++) {
      if (current.data === data) {
        if (this.length == 1) {
          this.head = this.tail = null;
        } else {
          current.prev.next = current.next;
        }
        this.length--;
        return;
      }
      current = current.next;
    }
  }
}

module.exports = LinkedList;

if (require.main === module) {
  var list = new LinkedList();
  list.push(20);
  list.push(10);
  list.delete(10);
  console.log(list);
}
