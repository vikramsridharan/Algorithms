class List:
  
  def __init__(self):
    self.root = None
    
  def add(self, value):
    i = Item(value, None)
    if self.root != None:
      i.next = self.root
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
    return self.internal_search(value, self.root)
  
  def get_predecessor(self, value, item):
    if ( item == None or item.next == None):
      return None
    if ( item.next.value == value ):
      return item
    else:
      return self.get_predecessor(value, item.next)
  
  def delete(self, value):
    if ( self.root == None ):
      print("Error: List is empty!")
      return None
    pred = self.get_predecessor(value, self.root)
    s = self.search(value)
    if s != None:
      if pred == None:
        self.root = s.next
      else:
        pred.next = s.next
          
class Item:
  
  def __init__(self, value, item):
    self.value = value
    self.next = item