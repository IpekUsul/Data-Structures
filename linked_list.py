class Node:
  """
  An object for a storing a single node of a linked list.
  Models two attributes - data and the link to the next node in the list

  """
  data=None
  next_node= None

def __init__(self, data):
  self.data=data

def __repr__(self):
  return "<Node data: %s> " % self.data

class LinkedList:
"""
singly lnked list
"""
  def __init__(self):
    self.head= None

  def is_empty(self):
    retrun self.head==None

  def size(self):
    """"
    returns the number of nodes in the list
    takes n(0) time
    """"
   
    current= self.head
    count=0
    
    while current:
      count+=1
      current= current.next_node

    return count

def add(self,data):
  """
  Adds new node containing data at head of the list
  Takes 0(1) time
  """
  new_node= Node(data)
  new_node.next_node=self.head
  self.head= new_node

 
