// Inside /src/utils/DoubleLinkedList.js

class ListNode {
    constructor(system) {
      this.system = system;
      this.next = null; // Forward connection
      this.prev = null; // Backward connection
    }
  }
  
  class DoubleLinkedList {
    constructor() {
      this.head = null;
      this.tail = null;
    }
  
    addNode(system) {
      const newNode = new ListNode(system);
      if (!this.head) {
        this.head = newNode;
        this.tail = newNode;
      } else {
        this.tail.next = newNode;
        newNode.prev = this.tail;
        this.tail = newNode;
      }
    }
  
    // Additional methods for managing nodes can be added here
  }
  