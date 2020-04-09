#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:30:12 2020

@author: shuyihuo
"""

import hashlib
import datetime


def calc_hash(data):
    sha = hashlib.sha256()
    hash_str = data.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()

class Block:

    def __init__(self, data, previous_hash):
      utc = datetime.datetime.utcnow()
      self.timestamp = utc
      self.data = data
      self.previous_hash = previous_hash
      self.hash = calc_hash(str(data))
      self.previous_block = None

    def printout(self):
        string = str(self.timestamp)+" \n" +str(self.data) +"\n "+ str(self.hash)+"\n " +str(self.previous_hash)+"\n "+str(self.hash)
        return string
  
class BlockChain:

    def __init__(self):

        self.head = None


    def append(self, data,previous_hash):

        #Append a block to the end of the chain

     
        if self.head is None:

          self.head = Block(data,0)

          return

        new_head = Block(data,self.head.hash)

        new_head.previous_block = self.head

      
        self.head = new_head   


    def toList(self):
    #return a list of blocks

      res = []

      block = self.head

      while block:

        res.append(block)

        block = block.previous_block

      return res
  

        
    
#Testing code
"""
Test Case1：
Check the empty blockchain and expected return none.
"""
print("Test Case 1 ")
testcase1 = BlockChain()
print(testcase1.head)
print()

"""
Test Case2:
Check one item in blockchain and expected return one Block object.
"""
print("Test Case 2 ")
testcase2 = BlockChain()
testcase2.append("Clare",0)
for item in testcase2.toList():
    print(item.printout())
print()

"""
Test Case3:
Check three items in blockchain and expected return three Block objects.
"""
print("Test Case 3 ")
testcase3 = BlockChain()
testcase3.append("Clare",0)
testcase3.append("Zoe",calc_hash("Clare"))
testcase3.append("Tom",calc_hash("Zoe"))

for item in testcase3.toList():
    print(item.printout())

print()


