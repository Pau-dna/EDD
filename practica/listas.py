
class SimpleNode:
    def __init__(self, data = None):
        self.data = data
        self._next = None
        
    # Getters and setters
    def getData(self):
        return self.data
    
    def getNext(self):
        return self._next
    
    def setData(self, data):
        self.data = data
        
    def setNext(self, nextNode):
        self._next = nextNode

class DoubleNode:
    def __init__(self, data = None):
        self.data = data
        self._next = None
        self._prev = None
        
    # Getters and setters
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data
    
    def getNext(self):
        return self._next
    
    def getPrev(self):
        return self._prev
        
    def setNext(self, nextNode):
        self._next = nextNode
        
    def setPrev(self, prev):
        self._prev = prev

class SimpleList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def size(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def setSize(self, size):
        self._size = size

    def first(self):
        return self._head
    
    def last(self):
        return self._tail

    def addFirst(self, data):
        node = SimpleNode(data)
        node.setNext(self._head)
        if self.isEmpty():
            self._tail = node
        self._head = node
        self._size += 1
        pass
    
    def addLast(self, data):
        node = SimpleNode(data)
        if self.isEmpty():
            self._tail = node
            self._head = node
        else:
            self._tail.setNext(node)
            self._tail = node
        self._size += 1
        pass
    
    def removeFirst(self):
        data = self._head.getData()
        self._head = self._head.getNext()
        self._size -= 1
        return data

    def removeLast(self):
        if self.size() == 1:
            return self.removeFirst()
        else:
            anterior = self._head
            while anterior.getNext() != self._tail:
                anterior = anterior.getNext()
            
            data = self._tail.getData()
            anterior.setNext(None)
            self._tail = anterior
            self._size -= 1
            return data
    
    def printData(self):
        node = self._head
        while node != None:
            print(node.getData())
            node = node.getNext()
        pass

class DoubleList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def size(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    def first(self):
        return self._head
    def last(self):
        return self._tail
    
    def addFirst(self, data):
        node = DoubleNode(data)
        node.setNext(self._head)        
        if self.isEmpty():
            self._tail = node
        else:
            self._head.setPrev(node)
        self._head = node
        self._size += 1
        pass
    
    def addLast(self, data):
        node = DoubleNode(data)
        if self.isEmpty():
            self._head = node
        else:
            node.setPrev(self._tail)
            self._tail.setNext(node)
        self._tail = node
        self._size += 1
        pass
        
    def removeFirst(self):
        data = self._head.getData()
        self._head = self._head.getNext()
        self._head.setPrev(None)
        self._size -= 1
        return data
    
    def removeLast(self):
        data = self._tail.getData()
        self._tail = self._tail.getPrev()
        self._tail.setNext(None)
        self._size -= 1
        return data

    def remove(self, node):
        if node == self._head:
            return self.removeFirst()
        elif node == self._tail:
            return self.removeLast()
        else:
            data = node.getData()

            prev = node.getPrev()
            nextNode = node.getNext()
            prev.setNext(nextNode)
            nextNode.setPrev(prev)

            self._size -= 1
            return data
        
    def addAfter(self, node, data):
        newNode = DoubleNode(data)
        newNode.setPrev(node)
        newNode.setNext(node.getNext())

        node.getNext().setPrev(newNode)
        node.setNext(newNode)
        self._size += 1
        pass

    def addBefore(self, node, data):
        newNode = DoubleNode(data)

        newNode.setNext(node)
        newNode.setPrev(node.getPrev())

        node.getPrev().setNext(newNode)
        node.setPrev(newNode)
        self._size += 1
        pass

    def printData(self):
        node = self._head
        while node != None:
            print(node.getData())
            node = node.getNext()
        pass