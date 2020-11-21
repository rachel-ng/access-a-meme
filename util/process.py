#!/usr/bin/python3

import sys, os, copy
import string

def process_chars():
    fin = open("chars.txt")

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
    fin = open("map.csv")

    raw = [i.replace(" ","").split(",") for i in fin.read().split("\n") if i != ""]
    mappings = {i[0]:i[1] for i in raw}
    print(mappings)
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
    return n 

m = "𝔱𝔥𝔦𝔰 𝔦𝔰 𝔫𝔬𝔱 𝔞𝔠𝔠𝔢𝔰𝔰𝔦𝔟𝔩𝔢! \n ⓘ  𝗢𝗳𝗳𝗶𝗰𝗶𝗮𝗹 𝘀𝗼𝘂𝗿𝗰𝗲𝘀 𝘀𝘁𝗮𝘁𝗲𝗱 𝘁𝗵𝗮𝘁 𝘁𝗵𝗶𝘀 𝗶𝘀 𝘁𝗿𝘂𝗲 \n 𝕥𝕙𝕚𝕤 𝕚𝕤 𝕒𝕔𝕔𝕖𝕤𝕤𝕚𝕓𝕝𝕖! \n ⓘ  𝗢𝗳𝗳𝗶𝗰𝗶𝗮𝗹 𝘀𝗼𝘂𝗿𝗰𝗲𝘀 𝘀𝘁𝗮𝘁𝗲𝗱 𝘁𝗵𝗮𝘁 𝗶𝘀 𝗳𝗮𝗹𝘀𝗲 𝗮𝗻𝗱 𝗺𝗶𝘀𝗹𝗲𝗮𝗱𝗶𝗻𝗴"
print(m)
print(remap(m))




