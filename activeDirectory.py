#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:12:33 2020

@author: shuyihuo
"""

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


 
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
         exist = True
         return(exist)
    else:
        if len(group.get_groups()) == 0:
            return False
        
        for i in group.get_groups():
             if is_user_in_group(user, i):
                  return(True)
    return False
    

'''
Test part:
'''       

        
'''   
Test case1:
    Test the function if it is work for checking user in group.
    Expected return: True
    
'''  
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group(sub_child_user,parent))
print()

'''   
Test case2:
    Test the function if it is work for checking user not in group.
    Expected return: False
    
'''

print(is_user_in_group("sub",parent))
print()

'''   
Test case3:
    Test the function if it is work for checking user in multiple groups.
    Expected return: True
    
'''
parent = Group("parent")
child1 = Group("child1")
child2 = Group("child2")

sub_child = Group("subchild")

sub_child.add_user("sub_child_user1")

sub_child_user = "sub_child_user2"
sub_child.add_user(sub_child_user)

child2.add_user("sub_child_user1")
child2.add_group(sub_child)
parent.add_group(child1)
parent.add_group(child2)        


print(is_user_in_group("sub_child_user1",parent))





