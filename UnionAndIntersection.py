#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 21:28:23 2020

@author: shuyihuo
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    if llist_1.size()<=0 and llist_2.size()<=0:
        return "The list is none."   
    set1 = set()
    set2 = set()
    cur1 = llist_1.head
    cur2 = llist_2.head
    
    while cur1 is not None:        
        set1.add(cur1.value)
        cur1 = cur1.next
        
    while cur2 is not None:
        set2.add(cur2.value)
        cur2 = cur2.next
        
    u = set1.union(set2)
    union = LinkedList()
    for item in u:
        union.append(item)
    
    return union
        

def intersection(llist_1, llist_2):
    # Your Solution Here
    if llist_1.size()<=0 and llist_2.size()<=0:
        return "The list is none."
    
    set1 = set()
    set2 = set()
    
    cur1 = llist_1.head
    cur2 = llist_2.head
    
    while cur1 is not None:
        set1.add(cur1.value)
        cur1 = cur1.next
        
    while cur2 is not None:
        set2.add(cur2.value)
        cur2 = cur2.next
        
    i = set1.intersection(set2)
    
    if len(i) == 0:
        return "There is no intersection between list_1 and list_2."
    
    intersection = LinkedList()
    for item in i:
        intersection.append(item)
    
    return intersection


'''
Test case 1:
    The case tests if the union function and intersection function work well 
    and the expected value is:
    The union is  32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 
    The intersection is  4 -> 21 -> 6 -> 
    
'''
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print ("The union is ",union(linked_list_1,linked_list_2))
print ("The intersection is ",intersection(linked_list_1,linked_list_2))

'''
# Test case 2:
    The case tests if the intersection of two lists exist
    and the expected value is:
    The union is  65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 
    The intersection is  There is no intersection between list_1 and list_2.
'''
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ("The union is ",union(linked_list_3,linked_list_4))
print ("The intersection is ",intersection(linked_list_3,linked_list_4))

'''
# Test case 3:
    The case tests if two empty lists have unon or intersection and the expected value is:
    The union is  The list is none.
    The intersection is  The list is none.
'''

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ("The union is ",union(linked_list_3,linked_list_4))
print ("The intersection is ",intersection(linked_list_3,linked_list_4))


    