
class Node:
    def __init__(self,value):
        self.value = value
        self.next  = None

class LinkedList:
    def __init__(self,value):  
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
       new_node = Node(value)
       if self.head is None:
        self.head = new_node
        self.tail = new_node
        self.length = 1
       else:
        self.tail.next = new_node
        self.tail = new_node       
        self.length = self.length + 1

    def pop(self):
        temp = self.head     
        if self.head == self.tail:
            last_node = self.head
            self.head = None
            self.tail = None
            print("List has only 1 item")
            return(last_node) 
        else:    
            while temp is not None:
                if temp.value == self.tail.value:                    
                    last_node = temp
                    pre.next  = None
                    self.tail = pre
                    self.length = self.length - 1
                    return(last_node)
                  
                else:
                    pre = temp
                    temp = temp.next

    def pop_improved(self):
        temp = self.head
        pre = temp
        if self.length == 0:
            return None
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length = self.length - 1
        if self.length == 0:
            self.tail = None
            self.head = None
        return temp

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        temp = self.head
        if self.length == 0:
            return None
        elif self.length == 1:           
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
        self.length -= 1
        return temp

    def get(self,value):
        temp = self.head
        while(temp.value != value):
            temp = temp.next
        return temp


mylinkedlist = LinkedList(1)
mylinkedlist.append(2)
mylinkedlist.append(3)
mylinkedlist.prepend(5)
mylinkedlist.print_list()
print(mylinkedlist.pop_first().value)
print(mylinkedlist.pop_improved().value)
print(mylinkedlist.get(1).value)




