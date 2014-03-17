#coding=utf-8
__author__ = 'Administrator'

#get 90% line value from a list with 10000 elements
import random
list1=[]
for i in range(100000):
    list1.append(random.randint(1,100000010))
list1.sort()
print list1[int(len(list1)*0.5)-1]
print list1[int(len(list1)*0.6)-1]
print list1[int(len(list1)*0.7)-1]
print list1[int(len(list1)*0.8)-1]
print list1[int(len(list1)*0.9)-1]
print list1[int(len(list1)*0.95)-1]
