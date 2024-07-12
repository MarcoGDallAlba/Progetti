#!/usr/bin/python

def de(s):
    z = [s[i] for i in range(0,len(s))]
    t = 1
    for k in range(0,25):
        for i in range(0,len(z)):
                if ord(z[i]) in range(97,123):
                    z[i] = chr((ord(z[i][0])-97-t)%26+97)
        code = ''.join(z) 
        print (k+1,code)
      
