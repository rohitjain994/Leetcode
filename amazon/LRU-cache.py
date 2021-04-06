class Node:
    def __init__(self,key=0,value=0,prv=None,next=None):
        self.key = key
        self.value = value
        self.prv = prv
        self.next = next
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = collections.OrderedDict()
        self.size = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prv = self.head
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            #remove from list
            node.next.prv = node.prv
            node.prv.next = node.next
            #add node to front
            head = self.head.next
            head.prv = node
            node.next = head
            node.prv = self.head
            self.head.next = node
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        node = Node(key,value)
        # if key already exist in cache retain same value
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            #remove from list
            node.next.prv = node.prv
            node.prv.next = node.next
            #current size
            self.size -=1
        elif self.size == self.cap:
            #delete last node
            tail = self.tail.prv
            tail.prv.next = self.tail
            self.tail.prv = tail.prv
            #clean cache
            self.cache.pop(tail.key)
            self.size -=1
        #add node to front
        head = self.head.next
        head.prv = node
        node.next = head
        node.prv = self.head
        self.head.next = node
        #add node to cache
        self.cache[key] = node
        self.size +=1
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)