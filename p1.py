# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 22:50:43 2018

@author: Kishan Kumar
"""

from nltk.corpus import stopwords



stop_words=set(stopwords.words('english'))

filename="testfile1.txt"
file1=open(filename,"r")

filteredFile = open("filtered.txt","w+")

line=file1.read()
words=line.split()

list1=[]

for r in words: 
    if not r in stop_words: 
       list1.append(r) 
       filteredFile.write("%s \n" % r)

for i in list1:
    print(i)