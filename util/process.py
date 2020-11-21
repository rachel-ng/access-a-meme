#!/usr/bin/python3

import sys, os, copy
import string
import re

DIR = os.path.dirname(__file__) or '.'
DIR += '/'

def process_chars():
    fin = open(DIR+"chars.txt")

    raw = [i.replace("'","").replace(" ","").split(",") for i in fin.read().split("\n") if i != ""]
    raw = [[j for j in i] for i in raw]

    u = list(string.ascii_uppercase) 
    l = list(string.ascii_lowercase) 
    d = list(string.digits) 

    #print(u)
    #print(l)
    #print(d)

    upper = {i:[] for i in u}
    lower = {i:[] for i in l}
    digits = {i:[] for i in d}

    u2 = {}
    l2 = {}
    d2 = {}

    mappings = {}

    for i in range(len(raw)): 
        if i % 3 == 0:
            #print("upper",u)
            for j in range(len(raw[i])):
                upper[u[j]] += [raw[i][j]]
                u2[raw[i][j]] = u[j]
                mappings[raw[i][j]] = u[j]

        if i % 3 == 1:
            #print("lower",l)
            for j in range(len(raw[i])):
                lower[l[j]] += [raw[i][j]]
                l2[raw[i][j]] = l[j]
                mappings[raw[i][j]] = l[j]

        if i % 3 == 2:
            #print("digit",d)
            for j in range(len(raw[i])):
                digits[d[j]] += [raw[i][j]]
                d2[raw[i][j]] = d[j]
                mappings[raw[i][j]] = d[j]

        '''
            s = ""
            for j in raw[i]:
                s += j + ", "
            print(s)
        '''
    output(mappings, "out.csv")


def output (dct, out):
    s = ""
    for i in dct: 
        s += i + ", " + dct[i] + "\n"
    f = open(out, "w")
    f.write(s)
    f.close()

def print_all (dct):
    for i in dct:
        s = ""
        for j in dct[i]:
            s += j + ", "
        print(s)
    print("\n")
#print_all(upper)
#print_all(lower)
#print_all(digits)

def print_ind (dct):
    for i in dct:
        print(i)
        print(dct[i])
#print_ind(u2)
#print_ind(l2)
#print_ind(d2)



def process_chars():
    fin = open(DIR+"map.csv")

    raw = [i.replace(" ","").split(",") for i in fin.read().split("\n") if i != ""]
    mappings = {i[0]:i[1] for i in raw}
    #print(mappings)
    return mappings


mappings = process_chars()

def print_maps():
    for i in mappings:
        s = i + ": " + mappings[i]
        print(s)

def remap (s):
    n = ""
    for i in s:
        n += mappings.get(i,i) 
    return n.replace('\n', '<br>') 

def process_tweets(timeline):
	for tweet in timeline:
		if tweet.user.name:
			#print(tweet.user.name)
			tweet.user.name=remap(tweet.user.name)
		if tweet.text:
			tweet.textold=tweet.text
			tweet.text=remap(tweet.text)
			#print(tweet.text)
	return timeline





