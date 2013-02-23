'''
Created on Dec 29, 2012

@author: Sanjeev Srivatsa
'''
import sys

#finds the overlap between two strings, and returns the way they are overlapped to be used to combine later
def match(s1, s2):
    count1 = 0;
    i = 0;
    j = 0;
    s1_len = len(s1)
    s2_len = len(s2)
    while i < s1_len and j < s2_len:
        if s1[i] == s2[j]:
            count1 += 1
            i += 1
            j += 1
        else:
            count1 = 0
            j = 0
            i += 1
    count2 = 0;
    i = 0;
    j = 0;
    while i < s2_len and j < s1_len:
        if s2[i] == s1[j]:
            count2 += 1
            i += 1
            j += 1
        else:
            count2 = 0
            j = 0
            i += 1
    if count1 > count2:
        return {"overlap" : count1, "type": True} #type is for whether its a left/right overlap, True if left overlap
    else:
        return {"overlap" : count2, "type": False}

#combines two strings assuming the right of the first one overlaps with the left of the second one given the overlap length
def combine(s1, s2, overlap):
    s = ""
    #special cases if one string completely contains the other, only print out the larger string
    if overlap == len(s1):
        return s2
    elif overlap == len(s2):
        return s1
    s += s1[:(len(s1)-overlap)]
    s += s2
    return s

#reassembles a document based on the fragments separated by semicolons
def reassemble(line):
    frags = line.split(";")
    #variables to keep track of two indices with longest overlap
    loc1 = 0
    loc2 = 0
    size = len(frags)
    while size > 1:
        max_overlap = 0
        for i in xrange(size):
            for j in xrange(i + 1, size):
                overlap = match(frags[i], frags[j])
                if overlap['overlap'] > max_overlap:
                    max_overlap = overlap['overlap']
                    if overlap['type']: #if left overlap
                        loc1 = i
                        loc2 = j
                    else:
                        loc1 = j
                        loc2 = i
        frags[loc1] = combine(frags[loc1], frags[loc2], max_overlap)
        frags[loc2] = frags[size - 1]
        frags.pop()
        size -= 1
    return frags[0]

file = open("test_cases.txt")

for line in file:
    line = str(line)
    line = line[:-1]
    print reassemble(line)
file.close()
sys.exit()
