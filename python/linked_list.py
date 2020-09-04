class Node:
    slots = '_data', '_next'
    def __init__(self, _data):
        self._data = _data
        self._next = None

class LinkedList:
    def __init__(self):
        self._head = None

    def printList(self):
        temp = self._head
        while (temp):
            print(temp._data)
            temp = temp._next

    def push(self, data):
        node = Node(data)
        node._next = self._head
        self._head = node
    
    def insertAfter(self, prev_node, data):
        if prev_node == None:
            print("INVALID PREVIOUS NODE")
            return
        
        node = Node(data)
        node._next = prev_node._next
        prev_node._next = node
    
    def append(self, data):
        node = Node(6)
        if self._head == None:
            self._head = node
        
        temp = self._head
        while temp._next != None:
            temp = temp._next
        temp._next = node

    def delete(self, data):
        temp = self._head
        if temp == None:
            print("Data Not Found")
            return
        
        if temp._data == data:
            self._head = temp._next
            temp = None
            return
         
        prev = temp 
        temp = prev._next
        while temp != None:
            if temp._data == data:
                prev._next = temp._next
                temp = None
                return
            prev = temp
            temp = temp._next
        
        print('Data Not Found')

    def reverse(self):
        prev = None
        curr = self._head

        while curr != None:
            next = curr._next
            curr._next = prev
            prev = curr
            curr = next
        
        self._head = prev 
    
    def reverseUtil(self, prev, curr):
        if curr._next == None:
            self._head = curr
            curr._next = prev
            return
        next = curr._next
        curr._next = prev
        
        self.reverseUtil(curr, next)

    def recReverse(self):
        if self._head == None:
            return
        self.reverseUtil(None, self._head)

    def sortedList(self, left, right):
        result = None
        if left == None:
            return right
        
        if right == None:
            return left
        
        if left._data <= right._data:
            result = left
            result.next = self.sortedList(left._next, right)
        else:
            result = right
            result.next = self.sortedList(left, right._next)
        return result
    
    def mergeSort(self, h):
        if h == None or h._next == None:
            return h
        
        middle = self.middleElement(h)
        nextToMiddle = middle._next
        middle._next = None
        
        left = self.mergeSort(h)
        right = self.mergeSort(nextToMiddle)

        sortedList = self.sortedList(left, right)
        # sortedList.printList()
        return sortedList
    
    def middleElement(self, head):
        if (head == None): 
            return head
        slow = head
        fast = head
        while fast._next != None and fast._next._next != None:
            slow = slow._next
            fast = fast._next._next
        return slow
    
if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    myLinkedList = LinkedList()
    myLinkedList._head = node1
    node1._next = node2
    node2._next = node3
    myLinkedList.push(4)
    # myLinkedList.printList()
    myLinkedList.insertAfter(node2, 5)
    # myLinkedList.printList()
    myLinkedList.append(6)
    # myLinkedList.printList()

    myLinkedList.delete(5)
    # myLinkedList.printList()
    # myLinkedList.reverse()
    # myLinkedList.printList()
    myLinkedList.recReverse()
    myLinkedList.printList()
    print("-------------------------------------------------------")
    # print(myLinkedList.middleElement(myLinkedList._head)._data)
    myLinkedList.head = myLinkedList.mergeSort(myLinkedList._head)
    myLinkedList.printList()
