class DoubleLinkedListNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"

class DoubleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""
        node = DoubleLinkedListNode(obj,None,None)

        if self.begin == None:
            self.begin = node
            self.end = node
        else:
            self.end.next = node
            node.prev = self.end
            self.end = node


    def pop(self):
        """Removes the last item and returns it."""
        if self.begin == None:
            return None

        if self.begin == self.end:
            data = self.begin.value
            self.begin = None
            self.end = None
            return data

        data = self.end.value
        prev = self.end.prev
        prev.next = None
        self.end = prev
        return data
        
    def shift(self, obj):
        """Actually just another name for push."""
        node = DoubleLinkedListNode(obj,None,None)

        if self.begin == None:
            self.begin = node
            self.end = node
        else:
            node.next = self.begin
            self.begin.prev = node
            self.begin = node

    def unshift(self):
        """Removes the first item (from begin) and returns it."""
        if self.begin == None:
            return None

        if self.begin == self.end:
            data = self.begin.value
            self.begin = None
            self.end = None
            return data

        data = self.begin.value

        self.begin = self.begin.next
        self.begin.prev = None

        return data

    def detach_node(self, node):
        """You'll need to use this operation sometimes, but mostly
        inside remove(). It should take a node, and detach it from the
        list, whether the node is at the front, end, or in the middle."""

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        pos = 0
        if self.begin == None:
            return None 

        node = self.begin

        while node.value != obj:
            node = node.next
            pos += 1
        
        if node == self.begin:
            self.begin.prev = None
            self.begin = self.begin.next
            return pos

        if node == self.end:
            self.end = self.end.prev
            self.end.next = None
            return pos

        if node.prev != None and node.next != None:
            node.next.prev = node.prev
        
        if node.next != None and node.prev != None:
            node.prev.next = node.next

        return pos


    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        if self.begin == None:
            return None
        else:
            return self.begin.value

    def last(self):
        """Returns a reference to the last item, does not remove."""
        if self.end == None:
            return None
        else:
            return self.end.value

    def count(self):
        """Counts the number of elements in the list."""
        if self.begin == None:
            return 0

        cnt = 1
        begin = self.begin

        while begin.next != None:
            begin = begin.next
            cnt +=1
        return cnt

    def get(self, index):
        """Get the value at index."""
        pos = 0
        if self.begin == None:
            return None

        node = self.begin
        while pos != index:
            if node.next == None:
                node = None
                break
            node = node.next
            pos += 1

        if node != None:
            return node.value
        else:
            return None

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        #self._invariant()

    def _invariant(self):
        """ invariant function for sanity check"""
        print('---------------------------')
        head = self.begin
        while head != None:
            print("head: ", head.value);
            if(head.prev != None):
                print("head.prev ", head.prev.value)
            if(head.next != None):
                print("head.next ", head.next.value)
            head = head.next
            print('------')

