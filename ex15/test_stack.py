from stack import *
 
def test_push( ):
    colors = Stack()
    colors.push("Pthalo Blue")
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    assert colors.count() == 2
    colors.dump()
    colors.push("White")
    colors.dump("____ before add Black")
    colors.push("Black")
    colors.dump("____ after add Black")
 
def test_pop( ):
    colors = Stack()
    colors.push("Magenta")
    colors.push("Alizarin")
    colors.push("Top")
 
    print(colors.pop())
 
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    assert colors.pop() == None
 

 
def test_count():
    colors = Stack()
    colors.push("Carbazole Violet")
    assert colors.count() == 1
    colors.push("Cadmium Orange")
    assert colors.count() == 2
 
    assert colors.pop() == "Cadmium Orange"
    assert colors.count() == 1
    assert colors.pop() == "Carbazole Violet"
    assert colors.count() == 0
 
 
def test_top():
    colors = Stack()
    colors.push("Cadmium Red Light")
    colors.dump()
    assert colors.top() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    assert colors.top() == "Hansa Yellow"
    colors.push("Pthalo Green")
    assert colors.top() == "Pthalo Green"

