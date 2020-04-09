#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 15:59:00 2020

@author: shuyihuo
"""


class LRU_Cache(object):
    
    
    
    def __init__(self, capacity):
        # Initialize class variables
        self.size = capacity
        self.dic = {}
        self.link =linkedList()
        


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        
        if key in self.dic: 
            out = self.dic[key]            
            self.link.prepend(self.dic[key])
            return out.value
        else:
            return -1
        

    
    def set(self, key, value):
        
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
          
        if len(self.dic) < self.size:           
            self.dic[key] = Node(key,value)            
            self.link.prepend(self.dic[key])
        else:
            self.dic[key] = Node(key,value)
            self.link.prepend(self.dic[key])
            removekey =  self.link.tail.key
            self.link.remove()
            self.dic.pop(removekey)
    
    def getValue(self):
        # print out the key and value to check the solution
        out = {}
        for key in self.dic:
             out[key] = self.dic[key].value
        return out


class Node:
    def __init__(self, key,value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None
        
    def removeLinks(self):
        if self.previous is not None:
            self.previous.next = self.next
        if self.next is not None:
            self.next.previous = self.previous
        self.previous = None
        self.next = None
        
class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    def append(self, value):
        """ Append a node to the end of the list """
        # Here I'm not keeping track of the tail. It's possible to store the tail
        # as well as the head, which makes appending like this an O(1) operation.
        # Otherwise, it's an O(N) operation as you have to iterate through the
        # entire list to add a new tail.
        new_node = Node(value)
        if self.head is None:
             self.head = Node(value)
             self.tail = self.head
             self.count += 1
             return
        else:    
             self.tail.next = new_node
             new_node.previous = self.tail 
             self.tail = new_node
             
        self.count += 1        
        return
        

       
    
    def size(self):
        """ Return the size or length of the linked list. """
        
        return self.count
    

        
    def prepend(self, node):
        """ Prepend a node to the beginning of the list """

        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.previous = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.remove()
            node.removeLinks()
            self.head.previous = node
            node.next = self.head
            self.head = node
        self.count += 1
        
    def remove(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.previous
        self.tail.next = None  
        self.count -= 1
        
        
    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out
    

'''
Test part:

'''            

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

'''
case 1: Expected output is {1: 1, 2: 2, 3: 3, 4: 4, 5: 5} 
and want to check the set function if could add element when the size is not 5.
 
'''
our_cache.set(5, 5) 
print('The linklist is {}'.format(our_cache.link.to_list()))
print('The dictionary is {}'.format(our_cache.getValue()))
print('\n')

'''
case 2: Expected output is -1  and want to check the get function.
 
'''
print('The value is {}'.format(our_cache.get(8))) 
print('\n')



'''
case 3: Expected output is {1: 1, 2: 2, 4: 4, 5: 5, 6: 6}
and want to check the set function if remove the least recently use element.
 
'''
our_cache.get(1)        # returns 1
our_cache.get(2)       # returns 2


our_cache.set(6, 6)
print('The linklist is {}'.format(our_cache.link.to_list()))
print('The dictionary is {}'.format(our_cache.getValue()))

print('The value is {}'.format(our_cache.get(3))) #should return -1
       






      