#!/usr/bin/python3
thestr = "Ogres are often foolhardy oafs"
newstr = ""
for i,c in enumerate(thestr):
    if c =="o":
        continue
    if i > 20:
        break
    newstr += c
    print(newstr)