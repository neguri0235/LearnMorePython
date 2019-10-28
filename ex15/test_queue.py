from queue import *
  
def test_push( ):
    colors = Queue()
    colors.push("AAA")
    assert colors.count() == 1
    colors.push("AAB")
    assert colors.count() == 2
    colors.push("AAC")
    colors.push("AAD")
    assert colors.count() == 4

def test_pop():
    colors = Queue()
    colors.push("AAA")
    colors.push("AAB")
    colors.push("AAC")
    assert colors.pop() == "AAA"
    assert colors.pop() == "AAB"
    assert colors.pop() == "AAC"
    assert colors.pop() == None

  
def test_front():
    colors = Queue()
    colors.push("AAA")
    assert colors.count() == 1
  
    colors.push("AAB")
    assert colors.count() == 2
  
    assert colors.front() == "AAA"
    assert colors.count() == 2
    assert colors.unshift() == "AAA"
    assert colors.front() == "AAB"
    assert colors.count() == 1

def test_back():
    colors = Queue()
  
    colors.push("AAA")
    colors.push("AAB")
    assert colors.back() == "AAB"
    colors.push("AAC")
    colors.push("AAD")
    assert colors.back() == "AAD"

def run_invariant():
    pass
