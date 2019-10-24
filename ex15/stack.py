
class StackNode(object):
 
    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt
 
    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"
 
 
class Stack(object):
 
    def __init__(self):
        self._top = None
        self.pos = 0
 
 
    def push(self, obj):
        """push new node to stack"""
        node = StackNode(obj,None)
        if self._top == None:
            self._top = node
        else:
            node.next = self._top
            self._top = node
        self.pos += 1
 
 
    def pop(self):
        """pop one node of stack and return"""

        if self._top == None:
            return None
        else:
            data = self._top.value
            self._top = self._top.next
            self.pos -= 1
            return data
 
 
    def top(self):
        """get top node of stack"""
        if self._top == None:
            return None
        else:
            return self._top.value
 
 
    def count(self):
        """return count of all stack element"""
        return self.pos

        '''
        cnt = 0
        node = self._top
        while node.next != None:
            node = node.next
            cnt+=1
        return cnt
        '''
 
 
    def dump(self, mark="----"):
        """debug function for showing all elements of all stack"""
        node = self._top

        while node:
            print(node.value)
            node = node.next
            
