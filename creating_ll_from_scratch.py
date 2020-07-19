#STEPS
#create Node class
#create Link class
# add node function
# delete node function (pop off the front)
# get value of current of head
# find length of linked list

#class names are usually nouns and functions are action names (verbs)
#they're nouns because they're blueprints for objects
# a method is a function that gets called on an object

# class Thing
#   def self.class_method
#
#   def instance_method
# end
#
# Thing.class_method

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return "<Node: value={} next={}>".format(self.value, self.next)

class LinkedList:
    # constructor
    def __init__(self):
        self.head = None

    def add(self, value):
        self.head = Node(value, self.head)

    def get_head_value(self):
        if self.empty():
            return None
        else:
            return self.head.value

    def length(self):
        current = self.head
        node_total = 0

        while current:
            node_total += 1
            current = current.next

        return node_total

    def pop(self):
        #identify the head
        #remember the head (store in a variable)
        #remove the head
        #resassign next value to head
        #return old head

        if self.empty():
            # raising an error would be better than a print because it raises
            #an exceptional problem with popping None
            raise IndexError('Your linked list is empty')

        head = self.head
        if self.head and self.head.next:
            self.head = self.head.next
        else:
            self.head = None
        return head.value

    def empty(self):
        return self.head == None



# usage

new_list = LinkedList()
print(new_list.get_head_value())
new_list.add("Bill")
print(new_list.get_head_value())
new_list.add("Amee")
print(new_list.get_head_value())
new_list.add("Alyson")
print(new_list.get_head_value())
print(new_list.length())
print(new_list.pop())
print(new_list.length())
print(new_list.pop())
print(new_list.length())
print(new_list.pop())
print(new_list.length())
print(new_list.pop())
print(new_list.length())


#
# class Noun:
#     def __init__(self, value, next):
#         pass
#
# my_variable = Noun(value, next)
# my_variable.add(value)
# print(my_variable.get_head_value())
