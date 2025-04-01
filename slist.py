class SList:
    class SListNode:
        def __init__ (self, value = None):
            self.value = value
            self.next = None

    def __init__ (self):
        self._head = None
        self._tail = None
        self._size = 0

    '''Insert a new value in the list. Maintain nondecreasing ordering of elements'''
    def insert(self, value):
        newNode = SList.SListNode(value)
        if self._head == None or self._head.value > newNode.value:
            if self._head == None:
                self._head = newNode
                self._head.next = None
                self._tail = self._head
            else:
                newNode.next = self._head
                self._head = newNode
        elif self._tail != None and newNode.value > self._tail.value:
            self._tail.next = newNode
            self._tail = newNode
        else:
            currentNode = self._head
            while currentNode.next != None and newNode.value >= currentNode.value and newNode.value >= currentNode.next.value:
                currentNode = currentNode.next
            if currentNode.next == None:
                self._tail = newNode
            newNode.next = currentNode.next
            currentNode.next = newNode
        self._size += 1

    '''Search for a value in the list, return it if found, None otherwise'''
    def find(self, value):
        currentNode = self._head
        while currentNode.value < value and (currentNode.value != value and currentNode != self._tail):
            currentNode = currentNode.next
        if currentNode.value == value:
            return currentNode.value
        else:
            return None

    '''Remove the first occurance of value.'''
    def remove(self, value):
        currentNode = self._head
        previousNode = None
        while currentNode.value < value and currentNode.value != value:
            if currentNode == self._tail:
                return False
            previousNode = currentNode
            currentNode = currentNode.next
        if currentNode.value == value:
            if currentNode == self._tail:
                previousNode.next = currentNode.next
                self._tail = previousNode
            elif currentNode == self._head:
                self._head = currentNode.next
            else:
                previousNode.next = currentNode.next 
            self._size -= 1
            return True
        else:
            return False

    '''Remove all instances of value'''
    def remove_all(self, value):
        loop = True
        while loop:
            loop = self.remove(value)

    '''Convert the list to a string and return it'''
    def __str__(self):
        string = "["
        currentNode = self._head
        while currentNode != self._tail:
            string += f"{currentNode.value}, "
            currentNode = currentNode.next
        string += f"{self._tail.value}]"
        return string

    '''Return an iterator for the list'''
    def __iter__(self):
        self._current = self._head
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        value = self._current.value 
        self._current = self._current.next
        return value

    '''Return the item at the given index, or throw an exception if invalid index'''
    def __getitem__(self, index):
        if index < 0:
            raise IndexError("Index must be non-negative")
                
        currentNode = self._head
        for _ in range(index):
            if currentNode is None:
                raise IndexError("Index out of range")
            currentNode = currentNode.next
        
        if currentNode is None:
            raise IndexError("Index out of range")
        
        return currentNode.value

    def size(self):
        return self._size
    
    def __len__(self):
        return self.size()
