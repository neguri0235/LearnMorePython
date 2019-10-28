class QueueNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"

class Queue(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""
        node = QueueNode(obj,None,None)

        if self.begin == None:
            self.begin = node
            self.end = node
        else:
            self.end.next = node
            node.prev = self.end
            self.end = node



        
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

    def pop(self):
        return self.unshift()

    def front(self):
        return self.first()

    def back(self):
        return self.last()

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

