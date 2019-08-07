class Item:
    def __init__(self, value, previous_item, next_item):
        self.value = value
        self.previous = previous_item
        self.next = next_item

class List:
    def __init__(self):
        self.root = None
    def add(self, value):
        if ( self.root == None ):
            i = Item(value=value, previous_item=None, next_item=None)
            self.root = i
        else:
            i = Item(value=value, previous_item=None, next_item=self.root)
            self.root.previous = i
            self.root = i
    def internal_search(self, value, item):
        if ( item == None):
            return None
        if ( item.value == value ):
            return item
        else:
            return self.internal_search(value, item.next)
    def search(self, value):
        if ( self.root == None ):
            print("Error: List is empty!")
            return None
        if ( self.root.value == value ):
            return self.root
        else:
            return self.internal_search(value, self.root.next)
    def delete(self, value):
        if (self.root != None):
            s =  self.search(value)
            if ( s != None ):
                previous = s.previous
                if ( s.next != None ):
                    if (previous != None):
                        previous.next = s.next
                        s.next.previous = previous
                    else:
                        s.next.previous = None
                        self.root = s.next
                else:
                    if ( previous != None ):
                        previous.next = s.next
                    else:
                        self.root = None



                 
                    
        

