#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 18:01:36 2020

@author: shuyihuo
"""

import sys

class Node:
    def __init__(self,char=None,num=None):
        self.char = char
        self.num = num
        self.right = None
        self.left = None
        
    def getNum(self):
        return self.num
    
    def getChar(self):
        return self.char
        
    def getLeft(self):
        return self.left
    
    def setLeft(self, left):
        self.left = left
        
    def getRight(self):
        return self.right
    
    def setRight(self, right):
        self.right = right
        
    def checkLeft(self):
        return self.left is not None
    
    def checkRight(self):
        return self.right is not None
    def printout(self):
        return (self.char,self.num)
    
    
    
class Tree:
    def __init__(self,node = None):
        self.root = node
        
    def getRoot(self):
        return self.root
    
    def setRoot(self,node):
        self.root = node
    

# Take a string and determine the relevant frequencies of the characters.    
def toMap(data):
    string = {}
    for item in data:

        if item in string.keys():
            string[item] +=1
        else:
            string[item] = 1
    return string

#Build and sort a list of tuples from lowest to highest frequencies.
def sort(string):
          
    return sorted(string.items(), key=lambda kv: kv[1])

def insertionSort(listnode, node):
    index = 0
    for i in range(len(listnode)):
        
        if(node.num>listnode[i].num):
           index = i+1
           
        else:
           
           listnode.insert(index, node) 
               
           break
       
        if(index >len(listnode)-1):
           
           listnode.append(node)
               
 # only for test code            
def visitList(l):
    for i in range(len(l)):
        print(l[i].printout())
    
    
def makeTree(data):
    # test if the data is none.
    if data == None or data == '':
        return "No characters enters."
    
    #sort the data and convers to list.  
    string = sort(toMap(data))
    myList=[]
    
    for i in range(len(string)):
        myList.append(Node(string[i][0],string[i][1]))
        
        
    # loop for make tree
    n = len(myList)
    i = 0
    while(i< n-1):
        left_node = myList.pop(0)
        right_node = myList.pop(0)
    
        fre = left_node.getNum()+right_node.getNum()
        parent_node = Node(char = "parent"+str(i),num = fre)
        parent_node.setRight(right_node)
        parent_node.setLeft(left_node)
        insertionSort(myList,parent_node)

        
        if(len(myList)==0):
            break
        
        i+=1
        
    
    tree = Tree(parent_node)
    return tree

        
codes = {}      
def huffman_encoding(data):
        # test if the data is valid.
    test = sort(toMap(data))
    if len(test)==1 or data == "":       
        return "Have to enter at least 2 different characters."
    
    codeIt('',makeTree (data).getRoot())
    string = ''
    for item in data:
        string = string+codes[item]
    
    return string, makeTree (data)
    

def codeIt(s, node):
	if len(node.char)==1:
		if not s:
			codes[node.char] = "0"
		else:
			codes[node.char] = s
	else:
		codeIt(s+"0", node.getLeft())
        
		codeIt(s+"1", node.getRight())
        
  
def huffman_decoding(data,tree):
    if(len(data)<2):
        return "illegal data and tree"
    
    cur = tree.getRoot()
    string = ""
    for item in data:
        
        
            
        if(item == '0'):

            cur = cur.getLeft()     

        else:

            cur = cur.getRight()
        
        if(cur.checkLeft()==False):
            
            string = string+ cur.getChar()
            cur = tree.getRoot()

        
    return string 
        


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    
'''   
test part: 
    
'''

'''   
case 1: Input content: "Hello world!" and expect output: "Hello world!"
    
'''
test = "Hello world!"
print('\n')
print(huffman_encoding(test))
res = huffman_encoding(test)
print(huffman_decoding(res[0],res[1]))
    
'''   
case 2: Input content: "" and 
        expect output: 'Have to enter at least 2 different characters.'
        This test checks the data if it is none.
    
'''
test = ""
print('\n')
print(huffman_encoding(test))
res = huffman_encoding(test)
print(huffman_decoding(res[0],res[1]))


'''   
case 3: Input content: "aaaaaa" and 
        expect output: 'Have to enter at least 2 different characters.'
        This test checks the data if it contains same character.
    
'''
test = "aaaaaa"
print('\n')
print(huffman_encoding(test))
res = huffman_encoding(test)
print(huffman_decoding(res[0],res[1]))





