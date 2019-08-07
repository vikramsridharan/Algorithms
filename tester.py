from unsorted_double_linked_list import List, Item

l = List()
l.add(1)
l.add(2)
l.add(3)
l.delete(4)
if ( l.search(4) != None):
    print(l.search(3).value)